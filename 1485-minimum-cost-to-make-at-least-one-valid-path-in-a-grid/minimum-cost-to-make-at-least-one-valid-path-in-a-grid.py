class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        RIGHT, LEFT, DOWN, UP = 1, 2, 3, 4
        DIRECTIONS = [RIGHT, LEFT, DOWN, UP]
        DIRECTION_DELTAS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        direction_to_delta = {
            RIGHT: (0, 1),
            LEFT: (0, -1),
            DOWN: (1, 0),
            UP: (-1, 0)
        }
        M, N = len(grid), len(grid[0])
        inBounds = lambda x, y: 0 <= x < M and 0 <= y < N

        fringe = collections.deque([(0, 0, 0)]) # Zero-One BFS!
        # visited = set()

        while len(fringe) > 0:
            # cost, x, y = heapq.heappop(fringe)
            cost, x, y = fringe.popleft()
            sign = grid[x][y]

            # Already found shoretst path to (x, y), so continue!
            # if (x, y) in visited:
            if sign == 0:
                continue

            # Found goal, return minimum cost!
            if x == M - 1 and y == N - 1:
                return cost
            
            # Otherwise mark (x, y) as visited since found shortest path to it,
            # and remember sign for rest of for loop!
            sign = grid[x][y]
            # visited.add((x, y))
            grid[x][y] = 0

            for direction in DIRECTIONS:
                dx, dy = DIRECTION_DELTAS[direction - 1]
                neigh_x, neigh_y = x + dx, y + dy
                if not inBounds(neigh_x, neigh_y) or grid[neigh_x][neigh_y] == 0:
                    continue
                
                if direction == sign:
                    fringe.appendleft((cost, neigh_x, neigh_y))
                else:
                    fringe.append((cost + 1, neigh_x, neigh_y))

        raise Exception("No Solution")
