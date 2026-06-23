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

for i in range(n):
    print(i, "->", adj[i])