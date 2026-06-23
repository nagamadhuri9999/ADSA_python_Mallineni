# Graph Properties, Types of Graphs, and Graph Terminology

## 1. Graph Terminology

A **Graph** $G$ is a pair of sets $(V, E)$, where $V$ is the set of vertices (nodes) and $E$ is the set of edges that connect pairs of vertices.

### Basic Terms:
*   **Vertex (Node):** The fundamental unit of a graph. Points where data can be stored.
*   **Edge (Link):** A connection between two vertices. An edge $(u, v)$ connects vertex $u$ and vertex $v$.
*   **Adjacent Vertices (Neighbors):** Two vertices are adjacent if there is a direct edge connecting them.
*   **Degree:** The number of edges connected to a vertex.
    *   **In-degree:** In a directed graph, the number of edges coming *into* a vertex.
    *   **Out-degree:** In a directed graph, the number of edges going *out of* a vertex.
*   **Path:** A sequence of vertices where each adjacent pair is connected by an edge.
*   **Path Length:** The number of edges in a path.
*   **Cycle:** A path that starts and ends at the same vertex, with no other repeated vertices or edges.
*   **Self-loop:** An edge that connects a vertex to itself.
*   **Connected Component:** A subgraph in which any two vertices are connected to each other by paths.

---

## 2. Types of Graphs

Graphs are categorized based on their edges, structure, and directionality.

### Based on Directionality:
1.  **Undirected Graph:** Edges have no direction. An edge $(u, v)$ is identical to $(v, u)$. 
    *   *Example:* Friendship network on Facebook (if A is friends with B, B is friends with A).
2.  **Directed Graph (Digraph):** Edges have a direction. An edge $(u, v)$ means the path goes from $u$ to $v$. 
    *   *Example:* Twitter followers (A follows B doesn't mean B follows A).

### Based on Weight:
3.  **Unweighted Graph:** All edges have the same default weight (usually 1). Only represents the presence of a connection.
4.  **Weighted Graph:** Each edge has a numerical value (weight/cost) associated with it.
    *   *Example:* Google Maps routes, where the weight is the distance or time between two cities.

### Based on Cycles:
5.  **Cyclic Graph:** A graph that contains at least one cycle.
6.  **Acyclic Graph:** A graph that contains NO cycles.
7.  **Directed Acyclic Graph (DAG):** A directed graph with no directed cycles.
    *   *Use Cases:* Task scheduling, Git commit history, resolving dependencies.

### Specialized Graphs:
8.  **Tree:** A connected acyclic undirected graph.
9.  **Forest:** A disconnected acyclic graph (a collection of disjoint trees).
10. **Bipartite Graph:** A graph whose vertices can be divided into two disjoint sets $U$ and $V$ such that every edge connects a vertex in $U$ to one in $V$.
11. **Complete Graph:** A graph in which every pair of distinct vertices is connected by a unique edge. A complete graph with $n$ vertices has $n(n-1)/2$ edges.

---

## 3. Key Graph Properties

1.  **Density:** The ratio of the number of edges $E$ to the maximal number of edges.
    *   **Dense Graph:** A graph where the number of edges is close to the maximum possible. $E \approx O(V^2)$. Better represented using an Adjacency Matrix.
    *   **Sparse Graph:** A graph where the number of edges is small compared to the maximum possible. $E \approx O(V)$. Better represented using an Adjacency List.
2.  **Connectivity:** 
    *   A graph is **Connected** if there is a path between every pair of vertices.
    *   A graph is **Disconnected** if it contains at least two unconnected vertices.
3.  **Eulerian Path & Circuit:**
    *   **Eulerian Path:** A path that visits every edge exactly once.
    *   **Eulerian Circuit:** An Eulerian path that starts and ends on the same vertex.
4.  **Hamiltonian Path & Circuit:**
    *   **Hamiltonian Path:** A path that visits every vertex exactly once.
    *   **Hamiltonian Circuit:** A Hamiltonian path that starts and ends on the same vertex. (The Traveling Salesperson Problem looks for the shortest Hamiltonian circuit in a weighted graph).
