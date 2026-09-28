#SLE-2: BFS vs DFS Profiling
#PRN : 25UAM090

1. Project Title

Performance Comparison of Breadth-First Search (BFS) and Depth-First Search (DFS)

2. Problem Statement

The objective of this experiment is to compare the performance of two uninformed search algorithms:

Breadth-First Search (BFS)
Depth-First Search (DFS)

A city-route graph is used to represent connections between cities. Both algorithms start from Pune and search for the goal city Ahmedabad.

The algorithms are compared using:

Average execution time
Number of nodes expanded
Whether the goal is found

The experiment uses Python's timeit module with 1000 repetitions to measure execution time.

3. Graph Used

The graph represents connections between cities:

Pune
├── Mumbai
│   ├── Surat
│   │   └── Vadodara
│   │       └── Ahmedabad
│   └── Kolhapur
│       └── Goa
│           └── Mangalore
└── Nashik
    └── Aurangabad
        └── Nagpur
            └── Bhopal

The graph is represented using a Python dictionary with an adjacency-list structure.

4. Algorithms Used
Breadth-First Search (BFS)

BFS uses a queue and explores nodes level by level.

In this project, Python's deque is used to implement the queue.

Depth-First Search (DFS)

DFS uses a stack and explores one branch deeply before backtracking.

In this project, a Python list is used as the stack.

5. Files in the Project
File	Description<br>
bfs_dfs.py	= Contains the BFS and DFS implementations and displays search results<br>
profile.py	= Measures BFS and DFS execution time using timeit<br>
profile.svg	= Visualization generated using py-spy<br>
README.md	= Project documentation<br>
AI_Contribution_Log.md	= Records the use of AI during development<br>
6. Experimental Configuration<br>
Parameter	Value<br>
Start Node	Pune<br>
Goal Node	Ahmedabad<br>
Repetitions	1000<br>
Programming Language	Python<br>
Timing Tool	timeit<br>
Profiling Tool	py-spy<br>
7. Experimental Results

The experiment was executed 1000 times.

Measure	BFS	DFS
Average Time	0.004536 ms	0.003086 ms
Nodes Expanded	10	5
Goal	Ahmedabad	Ahmedabad

Both algorithms successfully search from Pune to Ahmedabad.

For this particular graph and traversal order, DFS expanded fewer nodes and had a lower measured average execution time than BFS.

These results are specific to this experimental graph and configuration. They should not be interpreted as meaning that DFS is always faster than BFS.

8. Profiling Using py-spy

The py-spy tool was used to profile the Python program and generate a visualization of program execution.

Command used:

& "C:\Users\AppData\Local\Python\pythoncore-3.14-64\Scripts\py-spy.exe" record -o profile.svg -- python profile.py

The generated file is:

profile.svg

The SVG profiling output helps visualize where the Python program spends its execution time.

9. How to Run the Project
Step 1: Run the BFS and DFS program
python bfs_dfs.py
Step 2: Run the performance comparison
python profile.py
Step 3: Generate the py-spy profile
& "C:\Users\AppData\Local\Python\pythoncore-3.14-64\Scripts\py-spy.exe" record -o profile.svg -- python profile.py
Step 4: Open the profiling result
start profile.svg
10. Conclusion

The experiment demonstrates that BFS and DFS can show different performance results depending on the structure of the graph, the starting node, the goal node, and the traversal order.

For the selected city-route graph:

BFS expanded 10 nodes.
DFS expanded 5 nodes.
BFS average time was 0.004536 ms.
DFS average time was 0.003086 ms.
Both algorithms successfully found the goal city Ahmedabad.

Therefore, the experiment shows the importance of measuring algorithm performance using actual data instead of assuming that one search algorithm will always perform better.

11. Tools and Technologies
Python
collections.deque
timeit
py-spy
Git
GitHub
VS Code
