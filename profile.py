from collections import deque
import timeit

# City route graph
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


def bfs(start, goal):
    queue = deque([start])
    visited = set([start])
    nodes_expanded = 0

    while queue:
        node = queue.popleft()
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return nodes_expanded


def dfs(start, goal):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        # Reverse order so DFS follows the graph consistently
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

    return nodes_expanded


# Profiling configuration
START = "Pune"
GOAL = "Ahmedabad"
REPETITIONS = 1000


def run_bfs():
    bfs(START, GOAL)


def run_dfs():
    dfs(START, GOAL)


# Measure execution time
bfs_time = timeit.timeit(run_bfs, number=REPETITIONS)
dfs_time = timeit.timeit(run_dfs, number=REPETITIONS)

# Calculate average time
bfs_average = (bfs_time / REPETITIONS) * 1000
dfs_average = (dfs_time / REPETITIONS) * 1000

# Get node counts
bfs_nodes = bfs(START, GOAL)
dfs_nodes = dfs(START, GOAL)


print("=" * 45)
print("SLE-2: BFS vs DFS PROFILING")
print("=" * 45)

print(f"Start Node       : {START}")
print(f"Goal Node        : {GOAL}")
print(f"Repetitions      : {REPETITIONS}")

print("\nBFS")
print(f"Average Time     : {bfs_average:.6f} ms")
print(f"Nodes Expanded   : {bfs_nodes}")

print("\nDFS")
print(f"Average Time     : {dfs_average:.6f} ms")
print(f"Nodes Expanded   : {dfs_nodes}")

print("\nProfiling completed successfully.")