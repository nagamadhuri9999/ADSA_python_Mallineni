from collections import deque

def build_graph(n, edges):
    graph = [[0] * n for i in range(n)]
    for u, v in edges:
        graph[u][v] = 1
        graph[v][u] = 1
    return graph
edges=[[1,0],[2,3],[1,2]]
graph=build_graph(4,edges)
def print_graph(graph):
    print("Adjacency Matrix:")
    for row in graph:
        print(row)
print_graph(graph)