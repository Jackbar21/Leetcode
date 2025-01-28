class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        LAND = 0
        M, N = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Once we visit / "consume" a cell, we will set it to a LAND cell to effectively
        # mark it as "visited" :)
        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == LAND:
                    continue
                
                num_fish = grid[i][j]
                grid[i][j] = LAND

                stack = [(i, j)]
                while len(stack) > 0:
                    x, y = stack.pop()

                    for dx, dy in DIRECTIONS:
                        neigh_x, neigh_y = x + dx, y + dy
                        if neigh_x < 0 or neigh_x >= M or neigh_y < 0 or neigh_y >= N:
                            # Not in bounds, so ignore!
                            continue
                        if grid[neigh_x][neigh_y] == LAND:
                            continue
                        
                        num_fish += grid[neigh_x][neigh_y]
                        grid[neigh_x][neigh_y] = LAND
                        stack.append((neigh_x, neigh_y))
                
                if res < num_fish:
                    res = num_fish

        return res
