from collections import deque

n = 5

adj = [[] for _ in range(n)]

edges = [
    [1,0],
    [2,3],
    [1,3]
]

for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

print("Adjacency List:")

for i in range(n):
    print(i, "->", adj[i])


# ---------------- DFS ----------------

def dfs(start):

    visited = [False] * n

    stack = [start]

    print("\nDFS Traversal:")

    while stack:

        node = stack.pop()

        if not visited[node]:

            visited[node] = True

            print(node, end=" ")

            for neighbor in reversed(adj[node]):

                if not visited[neighbor]:
                    stack.append(neighbor)

    print()


# ---------------- BFS ----------------

def bfs(start):

    visited = [False] * n

    q = deque([start])

    visited[start] = True

    print("BFS Traversal:")

    while q:

        node = q.popleft()

        print(node, end=" ")

        for neighbor in adj[node]:

            if not visited[neighbor]:

                visited[neighbor] = True

                q.append(neighbor)

    print()


dfs(0)
bfs(0)