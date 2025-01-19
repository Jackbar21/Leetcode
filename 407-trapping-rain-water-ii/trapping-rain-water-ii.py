class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        grid = heightMap
        M, N = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # inBounds = lambda x, y: 0 <= x < M and 0 <= y < N

        fringe = [] # min-heap of borders
        # visited = set()
        # Instead of using a visited set, we can mark things visited
        # by setting grid[x][y] as -1 :)

        for i in range(M):
            heapq.heappush(fringe, (grid[i][0], i, 0))
            heapq.heappush(fringe, (grid[i][N - 1], i, N - 1))
            # visited.add((i, 0))
            # visited.add((i, N - 1))
            grid[i][0] = -1
            grid[i][N - 1] = -1
        for j in range(N):
            heapq.heappush(fringe, (grid[0][j], 0, j))
            heapq.heappush(fringe, (grid[M - 1][j], M - 1, j))
            # visited.add((0, j))
            # visited.add((M - 1, j))
            grid[0][j] = -1
            grid[M - 1][j] = -1
        
        res = 0
        while len(fringe) > 0:
            border_height, x, y = heapq.heappop(fringe)

            for dx, dy in DIRECTIONS:
                neigh_x, neigh_y = x + dx, y + dy
                # if (neigh_x, neigh_y) in visited or not inBounds(neigh_x, neigh_y):
                #     continue
                # visited.add((neigh_x, neigh_y))
                if not (0 <= neigh_x < M and 0 <= neigh_y < N) or grid[neigh_x][neigh_y] == -1:
                    continue
    
                neigh_height = grid[neigh_x][neigh_y]
                grid[neigh_x][neigh_y] = -1
                diff = border_height - neigh_height if border_height > neigh_height else 0

                res += diff
                heapq.heappush(fringe, (neigh_height + diff, neigh_x, neigh_y))

        return res
