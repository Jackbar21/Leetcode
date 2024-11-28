class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # return self.minimumObstaclesUCS(grid)
        return self.minimumObstaclesDijskstra(grid)
    
    def minimumObstaclesUCS(self, grid: List[List[int]]) -> int:
        # O(m * n * log(m * n))
        m, n = len(grid), len(grid[0])
        GOAL_STATE = (m - 1, n - 1)
        EMPTY, OBSTACLE = 0, 1
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # min heap / priority queue, (cost, (new_x, new_y))
        fringe = [(0, (0, 0))]
        # Shoutout to Mr. 'notbalding' on YouTube for suggesting to use an array of
        # booleans (instead of a hashset) for keeping track of visited/unvisited nodes :)
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        while True:
            cost, (x, y) = heapq.heappop(fringe)
            if (x, y) == GOAL_STATE:
                return cost

            for dx, dy in DIRECTIONS:
                pos = (x + dx, y + dy)
                new_x, new_y = pos
                if (0 <= new_x < m and 0 <= new_y < n 
                    and not visited[new_x][new_y]
                ):
                    visited[new_x][new_y] = True
                    is_obstacle = grid[new_x][new_y] == OBSTACLE
                    heapq.heappush(fringe, (cost + is_obstacle, pos))

        # raise Exception("Unreachable Code")
    
    def minimumObstaclesDijskstra(self, grid):
        # O(m * n * log(m * n))
        m, n = len(grid), len(grid[0])
        GRID_SIZE = m * n
        START_POSITION = (0, 0)
        GOAL_STATE = (m - 1, n - 1)
        EMPTY, OBSTACLE = 0, 1
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        d = {(x, y): float("inf") for x in range(m) for y in range(n)}
        d[START_POSITION] = 0
        min_heap = [(0, START_POSITION)] # (cost, position)
        visited = set([START_POSITION])
        while len(visited) < GRID_SIZE:
            cost, (x, y) = heapq.heappop(min_heap)
            if (x, y) == GOAL_STATE:
                # return cost
                break
            
            # assert cost <= d[(x, y)]
            # d[(x, y)] = cost
    
            # we JUST found the shortest path from START_POSITION to (x, y).
            # Now for each of (x, y)'s neighbors, i.e. up/down/left/right,
            # we want to update their optimal cost!
            for dx, dy in DIRECTIONS:
                pos = (x + dx, y + dy)
                new_x, new_y = pos
                # if (0 <= new_x < m and 0 <= new_y < n 
                #     and not visited[new_x][new_y]
                # ):
                if 0 <= new_x < m and 0 <= new_y < n and pos not in visited:
                    visited.add(pos)
                    is_obstacle = grid[new_x][new_y] == OBSTACLE
                    new_cost = cost + is_obstacle
                    if new_cost < d[(new_x, new_y)]:
                        d[(new_x, new_y)] = new_cost
                        heapq.heappush(min_heap, (new_cost, (new_x, new_y)))
        
        # print(f"{d=}")
        return d[GOAL_STATE]