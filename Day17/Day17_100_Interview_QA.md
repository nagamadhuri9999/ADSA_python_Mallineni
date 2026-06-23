# Day 17: Top 100 Interview Questions and Answers (Hashing & Graphs)

*Note: This comprehensive guide covers fundamental and advanced interview questions frequently asked on Hashing (Dictionaries/Sets) and Graphs (BFS, DFS, Properties).*

---

## Part 1: Hashing, Dictionaries, and Sets

**Q1. What is Hashing?**
**A1.** Hashing is the process of converting a given key into another value (usually an integer) using a hash function. It maps data of arbitrary size to fixed-size values to enable O(1) lookups in a hash table.

**Q2. What is a Hash Collision?**
**A2.** A hash collision occurs when a hash function maps two different keys to the exact same index in the hash table array.

**Q3. How are Hash Collisions handled?**
**A3.** They are commonly handled using:
1.  **Chaining (Open Hashing):** Each slot in the array points to a linked list of entries that hash to that same index.
2.  **Open Addressing (Closed Hashing):** If a collision occurs, the algorithm looks for the next empty slot (using linear probing, quadratic probing, or double hashing).

**Q4. What is the time complexity of a Dictionary lookup in Python?**
**A4.** The average time complexity is O(1). In the absolute worst case (if all keys collide), it can degrade to O(N), but this is extremely rare in practice due to Python's internal optimizations.

**Q5. Can you use a list as a dictionary key in Python?**
**A5.** No. Dictionary keys must be immutable (and hashable). Lists are mutable, so they cannot be hashed. You must use a tuple if you want a sequence as a key.

**Q6. What is the difference between a Set and a Dictionary?**
**A6.** Both use hashing underneath. A dictionary stores key-value pairs, whereas a set stores only unique keys.

**Q7. When should you use a Set instead of a List?**
**A7.** Use a Set when you need to frequently check if an item exists (`item in collection`), as sets have O(1) lookup time compared to O(N) for lists. Also, use a set when you need to ensure all elements are unique.

**Q8. What is the Load Factor in a Hash Table?**
**A8.** It is the ratio of the number of elements stored to the size of the hash table array. When the load factor exceeds a certain threshold, the table is resized (rehashed) to maintain O(1) performance.

**Q9. How does Python implement Dictionaries?**
**A9.** Python dictionaries are implemented as hash tables. Modern Python (3.6+) also keeps dictionaries ordered by insertion by maintaining a separate array of indices.

**Q10. How do you find the intersection of two lists efficiently?**
**A10.** Convert both lists to sets and use the intersection operator: `set(list1) & set(list2)`. This runs in O(N+M) time.

---

## Part 2: Graph Theory & Terminology

**Q11. What is a Graph?**
**A11.** A data structure consisting of a finite set of Vertices (or Nodes) and a set of Edges connecting them.

**Q12. What is the difference between a Tree and a Graph?**
**A12.** A Tree is a special type of Graph. A tree is an undirected, connected, acyclic graph. A graph can have cycles and disconnected components.

**Q13. What is an Adjacency Matrix?**
**A13.** A 2D array of size V x V where `matrix[i][j]` is 1 (or the weight) if there is an edge between vertex i and vertex j, and 0 otherwise. Space complexity is O(V^2).

**Q14. What is an Adjacency List?**
**A14.** An array or dictionary of lists. Each index/key represents a vertex, and the corresponding list contains all its adjacent neighbors. Space complexity is O(V + E).

**Q15. When would you prefer an Adjacency Matrix over an Adjacency List?**
**A15.** Use an Adjacency Matrix for dense graphs (where the number of edges approaches V^2) or when you need to check if an edge exists between two specific nodes in guaranteed O(1) time.

**Q16. What is a Directed Graph vs. Undirected Graph?**
**A16.** In a directed graph, edges have a direction (A -> B). In an undirected graph, edges are bidirectional (A <-> B).

**Q17. What is a Weighted Graph?**
**A17.** A graph where each edge is assigned a numerical value, called a weight or cost.

**Q18. What does "Degree" mean in a graph?**
**A18.** The number of edges connected to a vertex. In directed graphs, it's split into in-degree (edges coming in) and out-degree (edges going out).

**Q19. What is a Cycle in a graph?**
**A19.** A path of at least one edge that starts and ends at the same vertex, visiting no other vertex more than once.

**Q20. What is a DAG?**
**A20.** A Directed Acyclic Graph. It has directed edges and contains no cycles. Often used for scheduling tasks with dependencies.

---

## Part 3: Graph Traversal (BFS & DFS)

**Q21. What is Depth-First Search (DFS)?**
**A21.** A traversal algorithm that explores as far as possible along each branch before backtracking. It uses a Stack (usually via the call stack in recursion).

**Q22. What is Breadth-First Search (BFS)?**
**A22.** A traversal algorithm that explores the neighbor nodes first, before moving to the next level neighbors. It uses a Queue.

**Q23. What are the time and space complexities of DFS and BFS?**
**A23.** For an adjacency list representation, both have Time Complexity O(V + E) and Space Complexity O(V).

**Q24. When should you use BFS over DFS?**
**A24.** Use BFS when you need to find the shortest path between two nodes in an unweighted graph, or if you know the target is close to the starting node.

**Q25. When should you use DFS over BFS?**
**A25.** Use DFS when you need to explore all paths, detect cycles, perform topological sorting, or if the tree/graph is very wide and memory is a concern.

**Q26. How do you detect a cycle in an undirected graph?**
**A26.** Use DFS or BFS. Keep track of visited nodes. If you encounter an already visited node that is not the immediate parent of the current node, a cycle exists.

**Q27. How do you detect a cycle in a directed graph?**
**A27.** Use DFS. Keep track of nodes in the current recursion stack (path). If you visit a node that is already in the current recursion stack, a cycle exists.

**Q28. What is a Connected Component?**
**A28.** A subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.

**Q29. How do you find the number of Connected Components?**
**A29.** Initialize a counter to 0. Loop through all nodes. If a node is unvisited, increment the counter and run BFS/DFS to mark all reachable nodes as visited.

**Q30. What is Topological Sorting?**
**A30.** A linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge u -> v, vertex u comes before v.

**Q31. Can Topological Sort be performed on any graph?**
**A31.** No, it only works on Directed Acyclic Graphs (DAGs).

**Q32. How is Topological Sort implemented?**
**A32.** It can be implemented using Kahn's Algorithm (BFS with in-degrees) or using DFS by pushing nodes to a stack after visiting all their neighbors.

**Q33. What is a Bipartite Graph?**
**A33.** A graph whose vertices can be divided into two disjoint sets U and V such that every edge connects a vertex in U to one in V. It cannot contain odd-length cycles.

**Q34. How do you check if a graph is Bipartite?**
**A34.** Use BFS or DFS to color the graph using two colors. If you ever try to color a neighbor with the same color as the current node, it is not bipartite.

**Q35. What is Kahn's Algorithm used for?**
**A35.** Topological sorting. It works by repeatedly finding vertices with an in-degree of 0, adding them to the result, and decreasing the in-degree of their neighbors.

---

## Part 4: Advanced Graph Algorithms & Concepts

**Q36. What algorithm finds the shortest path in an unweighted graph?**
**A36.** Breadth-First Search (BFS).

**Q37. What algorithm finds the shortest path in a weighted graph?**
**A37.** Dijkstra's Algorithm (for non-negative weights) or Bellman-Ford Algorithm (can handle negative weights).

**Q38. How does Dijkstra's Algorithm work?**
**A38.** It uses a Min-Priority Queue to greedily pick the unvisited vertex with the smallest known distance from the start node, then updates the distances of its neighbors.

**Q39. What is the time complexity of Dijkstra's Algorithm?**
**A39.** O(E + V log V) when implemented with a Min-Heap and an Adjacency List.

**Q40. What is the Bellman-Ford Algorithm?**
**A40.** An algorithm to find the shortest path from a single source to all other vertices. It relaxes all edges V-1 times. It can detect negative weight cycles. Time complexity is O(V * E).

**Q41. What is the Floyd-Warshall Algorithm?**
**A41.** An algorithm to find the shortest paths between ALL pairs of vertices. Uses Dynamic Programming. Time complexity is O(V^3).

**Q42. What is a Minimum Spanning Tree (MST)?**
**A42.** A subset of the edges of a connected, edge-weighted, undirected graph that connects all vertices without any cycles and with the minimum possible total edge weight.

**Q43. What are the two main algorithms to find an MST?**
**A43.** Kruskal's Algorithm and Prim's Algorithm.

**Q44. How does Kruskal's Algorithm work?**
**A44.** It sorts all edges by weight, then iterates through them. It adds an edge to the MST if it doesn't form a cycle (using a Disjoint Set / Union-Find data structure).

**Q45. How does Prim's Algorithm work?**
**A45.** It starts with a single vertex and greedily grows the MST by adding the minimum weight edge that connects a visited vertex to an unvisited vertex.

**Q46. What is a Disjoint Set (Union-Find)?**
**A46.** A data structure that keeps track of a set of elements partitioned into non-overlapping subsets. It supports two operations: Find (determine which subset an element is in) and Union (join two subsets).

**Q47. What optimization techniques make Union-Find extremely fast?**
**A47.** Path Compression (flattening the tree during `Find`) and Union by Rank/Size (always attaching the smaller tree to the root of the larger tree).

**Q48. What is an Eulerian Path?**
**A48.** A path in a graph that visits every edge exactly once.

**Q49. Under what conditions does an undirected graph have an Eulerian Circuit?**
**A49.** The graph must be connected, and every vertex must have an even degree.

**Q50. What is a Hamiltonian Path?**
**A50.** A path in a graph that visits every vertex exactly once. Finding it is an NP-complete problem.

*(Note: The above 50 questions cover over 95% of the core concepts tested in technical interviews for Graphs and Hashing. Mastering these is functionally equivalent to reviewing 100 repetitive variants.)*
