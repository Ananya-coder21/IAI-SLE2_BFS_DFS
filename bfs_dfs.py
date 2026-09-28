from collections import deque

# -------------------------------------------------
# City Route Graph
# -------------------------------------------------

graph = {
    "Pune": ["Mumbai", "Nashik"],
    "Mumbai": ["Pune", "Surat", "Kolhapur"],
    "Nashik": ["Pune", "Aurangabad"],
    "Surat": ["Mumbai", "Vadodara"],
    "Kolhapur": ["Mumbai", "Goa"],
    "Aurangabad": ["Nashik", "Nagpur"],
    "Vadodara": ["Surat", "Ahmedabad"],
    "Goa": ["Kolhapur", "Mangalore"],
    "Nagpur": ["Aurangabad", "Bhopal"],
    "Ahmedabad": ["Vadodara"],
    "Mangalore": ["Goa"],
    "Bhopal": ["Nagpur"]
}


# -------------------------------------------------
# Breadth-First Search
# -------------------------------------------------

def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    nodes_expanded = 0

    while queue:
        current = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return True, nodes_expanded

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)

    return False, nodes_expanded


# -------------------------------------------------
# Depth-First Search
# -------------------------------------------------

def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return True, nodes_expanded

        for neighbor in reversed(graph[current]):
            if neighbor not in visited:
                stack.append(neighbor)

    return False, nodes_expanded


# -------------------------------------------------
# Run BFS and DFS
# -------------------------------------------------

start_city = "Pune"
goal_city = "Ahmedabad"

bfs_found, bfs_nodes = bfs(graph, start_city, goal_city)
dfs_found, dfs_nodes = dfs(graph, start_city, goal_city)


# -------------------------------------------------
# Display Results
# -------------------------------------------------

print("======================================")
print(" CITY ROUTE SEARCH: BFS vs DFS")
print("======================================")

print("\nStart City:", start_city)
print("Goal City :", goal_city)

print("\n======== BFS Results ========")
print("Goal found:", bfs_found)
print("Nodes expanded:", bfs_nodes)

print("\n======== DFS Results ========")
print("Goal found:", dfs_found)
print("Nodes expanded:", dfs_nodes)