class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:    
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
    