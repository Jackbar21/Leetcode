class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        GOAL_STATE = (M - 1, N - 1)
        DIRECTIONS = [(1, 0), (0, 1)] # only down or right

        fringe = [(grid[0][0], 0, 0)] # (cost, x, y)
        visited = set()
        while fringe:
            cost, x, y = heapq.heappop(fringe)
            if (x, y) in visited:
                continue
            visited.add((x, y))

            if (x, y) == GOAL_STATE:
                return cost
            
            for dx, dy in DIRECTIONS:
                neigh_x, neigh_y = x + dx, y + dy
                if neigh_x >= M or neigh_y >= N:
                    # Out of bounds
                    continue

                heapq.heappush(fringe, (cost + grid[neigh_x][neigh_y], neigh_x, neigh_y))
