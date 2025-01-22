class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        grid = isWater
        M, N = len(grid), len(grid[0])
        LAND, WATER = 0, 1
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # Idea: I got a little spoiled by the 'Note' section showing how this problem is
        # "the same" as problem 542. This problems suggests finding the nearest '0' cell for
        # each '1' cell, which in the context of this problem makes sense as it will be the
        # BOTTLENECK for any possible land cell to reach its maximal height.

        queue = collections.deque() # (closest_water_dist, i, j)
        closest_water = [[-1] * N for _ in range(M)] # -1 means 'unvisited'
        for i in range(M):
            for j in range(N):
                if grid[i][j] == WATER:
                    queue.append((0, i, j))
                    closest_water[i][j] = 0

        while len(queue) > 0:
            closest_water_dist, x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                neigh_x, neigh_y = x + dx, y + dy
                if 0 <= neigh_x < M and 0 <= neigh_y < N and closest_water[neigh_x][neigh_y] == -1:
                    # (neigh_x, neigh_y) in bounds AND not yet visited, so append to queue
                    # and mark its closest water distance (which also marks it visited!)
                    queue.append((closest_water_dist + 1, neigh_x, neigh_y))
                    closest_water[neigh_x][neigh_y] = closest_water_dist + 1

        return closest_water
