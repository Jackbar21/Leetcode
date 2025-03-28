class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        M, N = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        inBounds = lambda i, j: 0 <= i < M and 0 <= j < N

        sorted_queries = sorted(queries)
        solutions = {}

        fringe = [(grid[0][0], 0, 0)] # (grid[i][j], i, j)
        visited = set()
        for query in sorted_queries:
            if query in solutions:
                continue
            
            while fringe and fringe[0][0] < query:
                cost, i, j = heapq.heappop(fringe)
                if (i, j) in visited:
                    continue
                visited.add((i, j))

                for di, dj in DIRECTIONS:
                    neigh_i, neigh_j = i + di, j + dj
                    if not inBounds(neigh_i, neigh_j) or (neigh_i, neigh_j) in visited:
                        continue
                    neigh_cost = max(cost, grid[neigh_i][neigh_j])
                    heapq.heappush(fringe, (neigh_cost, neigh_i, neigh_j))
            
            solutions[query] = len(visited)
        
        return [solutions[query] for query in queries]
        