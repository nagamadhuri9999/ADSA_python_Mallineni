from collections import deque

def build_graph(n, edges):
    graph = [[0] * n for _ in range(n)]
    for u, v in edges:
        graph[u][v] = 1
        graph[v][u] = 1
    return graph

def print_graph(graph):
    print("Adjacency Matrix:")
    for row in graph:
        print(row)

def dfs(graph, start):
    n = len(graph)
    visited = [False] * n
    stack = [start]
    print("DFS Traversal:")
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(node, end=" ")
            for i in range(n - 1, -1, -1):
                if graph[node][i] == 1 and not visited[i]:
                    stack.append(i)
    print()

def bfs(graph, start):
    n = len(graph)
    visited = [False] * n
    q = deque([start])
    visited[start] = True
    print("BFS Traversal:")
    while q:
        node = q.popleft()
        print(node, end=" ")
        for i in range(n):
            if graph[node][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)
    print()

# ---------------- DRIVER CODE ----------------

n = 5
edges = [
    [1, 0],
    [2, 3],
    [1, 3]
]

graph = build_graph(n, edges)

print_graph(graph)
print()

dfs(graph, 0)
bfs(graph, 0)
