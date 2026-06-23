# Day 17: Easy Graph Problems on LeetCode with Solutions

from typing import List

class Solution:
    # ---------------------------------------------------------
    # 1. Find the Center of Star Graph (LeetCode 1791)
    # ---------------------------------------------------------
    # Problem: There is an undirected star graph consisting of n nodes labeled from 1 to n. 
    # A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.
    # You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. 
    # Return the center of the given star graph.
    
    def findCenter(self, edges: List[List[int]]) -> int:
        # Solution: The center node will appear in every edge. 
        # So we just need to compare the nodes of the first two edges.
        u1, v1 = edges[0]
        u2, v2 = edges[1]
        
        if u1 == u2 or u1 == v2:
            return u1
        return v1

    # Time Complexity: O(1) - we only check the first two edges.
    # Space Complexity: O(1)


    # ---------------------------------------------------------
    # 2. Find if Path Exists in Graph (LeetCode 1971)
    # ---------------------------------------------------------
    # Problem: There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). 
    # The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. 
    # Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
    # You want to determine if there is a valid path that exists from vertex source to vertex destination.
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import defaultdict, deque
        
        # Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # BFS Traversal
        queue = deque([source])
        visited = set([source])
        
        while queue:
            node = queue.popleft()
            
            if node == destination:
                return True
                
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return False
        
    # Time Complexity: O(V + E) where V is number of vertices and E is number of edges.
    # Space Complexity: O(V + E) for the adjacency list and queue/visited set.


    # ---------------------------------------------------------
    # 3. Find the Town Judge (LeetCode 997)
    # ---------------------------------------------------------
    # Problem: In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
    # If the town judge exists, then:
    # 1. The town judge trusts nobody.
    # 2. Everybody (except for the town judge) trusts the town judge.
    # 3. There is exactly one person that satisfies properties 1 and 2.
    # You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
    # Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Solution: Use in-degrees and out-degrees.
        # The judge will have an in-degree of n-1 and an out-degree of 0.
        
        if n == 1 and not trust:
            return 1
            
        trust_counts = [0] * (n + 1)
        
        for u, v in trust:
            trust_counts[u] -= 1  # Out-degree (trusts someone)
            trust_counts[v] += 1  # In-degree (is trusted by someone)
            
        for i in range(1, n + 1):
            if trust_counts[i] == n - 1:
                return i
                
        return -1

    # Time Complexity: O(E) where E is the number of trust relationships.
    # Space Complexity: O(N) for the trust_counts array.


    # ---------------------------------------------------------
    # 4. Flood Fill (LeetCode 733)
    # ---------------------------------------------------------
    # Problem: An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
    # You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
    # To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
    # plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image # Nothing to do
            
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != original_color:
                return
                
            image[r][c] = color # Fill color
            
            # Explore 4 directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            
        dfs(sr, sc)
        return image

    # Time Complexity: O(N) where N is the number of pixels in the image.
    # Space Complexity: O(N) for the recursive call stack in the worst case.


    # ---------------------------------------------------------
    # 5. Island Perimeter (LeetCode 463)
    # ---------------------------------------------------------
    # Problem: You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
    # Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island.
    # Determine the perimeter of the island.

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    # Check top neighbor
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2
                    # Check left neighbor
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2
                        
        return perimeter

    # Time Complexity: O(R * C) where R is rows and C is columns.
    # Space Complexity: O(1)
