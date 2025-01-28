class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        LAND = 0
        M, N = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        inBounds = lambda x, y: 0 <= x < M and 0 <= y < N
        
        # Once we visit / "consume" a cell, we will set it to a LAND cell to effectively
        # mark it as "visited" :)
        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == LAND:
                    continue
                
                num_fish = grid[i][j]
                grid[i][j] = LAND # Mark visited!

                stack = [(i, j)]
                while len(stack) > 0:
                    x, y = stack.pop()

                    for dx, dy in DIRECTIONS:
                        neigh_x, neigh_y = x + dx, y + dy
                        if not inBounds(neigh_x, neigh_y):
                            continue
                        if grid[neigh_x][neigh_y] == LAND:
                            continue
                        
                        num_fish += grid[neigh_x][neigh_y]
                        grid[neigh_x][neigh_y] = LAND # Mark visited!
                        stack.append((neigh_x, neigh_y))
                
                if res < num_fish:
                    res = num_fish

        return res
