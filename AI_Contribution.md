# AI Contribution Log

## SLE-2: BFS vs DFS Profiling

### Project

**Performance Comparison of BFS and DFS**


---

## 1. Purpose of AI Assistance

AI tools were used as a learning and development assistant during the implementation of the BFS vs DFS profiling experiment.

The student reviewed, understood, tested, and modified the generated suggestions before using them in the project.

---

## 2. AI Contributions

| Sr. No. | Project Part            | AI Assistance                                                                          | Student Contribution                                                                        |
| ------- | ----------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| 1       | Problem Understanding   | Explained the BFS vs DFS comparison problem in simple language.                        | Understood the problem and selected the city-route graph approach.                          |
| 2       | Graph Representation    | Suggested representing city connections using a Python dictionary and adjacency lists. | Created and modified the city graph used in the experiment.                                 |
| 3       | BFS                     | Provided guidance for implementing BFS using a queue and `deque`.                      | Reviewed, understood, tested, and modified the BFS implementation.                          |
| 4       | DFS                     | Provided guidance for implementing DFS using a stack.                                  | Reviewed, understood, tested, and modified the DFS implementation.                          |
| 5       | Node Counting           | Explained how to count expanded nodes during search.                                   | Implemented and verified node-counting logic.                                               |
| 6       | Performance Measurement | Suggested using Python's `timeit` module for repeated execution.                       | Set the experiment to 1000 repetitions and checked the output.                              |
| 7       | Profiling               | Explained how to use `py-spy` to generate a profiling visualization.                   | Installed/configured `py-spy`, executed the profiling command, and generated `profile.svg`. |
| 8       | Debugging               | Helped identify the `py-spy` PATH/executable-location issue.                           | Located the executable and successfully executed the profiling command.                     |
| 9       | Documentation           | Helped organize the README structure and explain the experimental results.             | Verified the actual results and included them in the documentation.                         |

---

## 3. AI-Generated Code

AI assistance was used for initial code ideas and explanations related to:

* BFS implementation
* DFS implementation
* Graph representation
* Node expansion counting
* `timeit` performance measurement
* py-spy profiling command

The generated suggestions were not accepted blindly. The code was reviewed, executed, tested, and modified according to the requirements of the experiment.

---

## 4. Student Ownership

The student was responsible for:

* Selecting the city-route graph problem
* Setting the start node as `Pune`
* Setting the goal node as `Ahmedabad`
* Choosing 1000 repetitions
* Running the Python programs
* Checking BFS and DFS results
* Installing and configuring py-spy
* Generating the profiling output
* Comparing the measured results
* Preparing the final project documentation
* Uploading and maintaining the project repository

---

## 5. Actual Experimental Output

The final experiment produced:

```text
=============================================
SLE-2: BFS vs DFS PROFILING
=============================================
Start Node       : Pune
Goal Node        : Ahmedabad
Repetitions      : 1000

BFS
Average Time     : 0.004536 ms
Nodes Expanded   : 10

DFS
Average Time     : 0.003086 ms
Nodes Expanded   : 5

Profiling completed successfully
```

---

## 6. Reflection

AI assistance helped in understanding the implementation and profiling process. The student learned how BFS uses a queue, how DFS uses a stack, how nodes can be counted during search, and how execution time can be measured using repeated runs.

The student also learned how to use `py-spy` to generate a profiling visualization and how to troubleshoot an executable PATH issue.

The final experimental results were obtained by executing the student's Python programs rather than by assuming the result from AI-generated information.
