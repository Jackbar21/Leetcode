class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # WALL_COST = len(grid) * len(grid[0]) + 1
        m, n = len(grid), len(grid[0])
        GOAL_STATE = (m - 1, n - 1)
        EMPTY, OBSTACLE = 0, 1
        DIRECTIONS = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        # O(m * n * log(m * n))
        fringe = [(0, (0, 0))] # min heap, (cost, (new_x, new_y))
        visited = set([(0, 0)]) # TODO: notbalding tip of the day: use boolean array

        while len(fringe) > 0: # TODO: Change to 'while True' since always sol'n!
            cost, (x, y) = heapq.heappop(fringe)
            if (x, y) == GOAL_STATE:
                return cost

            for dx, dy in DIRECTIONS:
                new_x, new_y = (x + dx, y + dy)
                if (0 <= new_x < m and 0 <= new_y < n 
                    and (new_x, new_y) not in visited
                ):
                    visited.add((new_x, new_y))
                    new_x, new_y = (new_x, new_y)
                    is_obstacle = grid[new_x][new_y] == OBSTACLE
                    heapq.heappush(fringe, (cost + is_obstacle, (new_x, new_y)))


            
        raise Exception("Unreachable Code")