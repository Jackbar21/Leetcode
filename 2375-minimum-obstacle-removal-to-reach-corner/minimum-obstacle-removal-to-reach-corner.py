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

        while True: # TODO: Change to 'while True' since always sol'n!
            cost, (x, y) = heapq.heappop(fringe)
            if (x, y) == GOAL_STATE:
                return cost

            for dx, dy in DIRECTIONS:
                pos = (x + dx, y + dy)
                new_x, new_y = pos
                if (0 <= new_x < m and 0 <= new_y < n 
                    and pos not in visited
                ):
                    visited.add(pos)
                    is_obstacle = grid[new_x][new_y] == OBSTACLE
                    heapq.heappush(fringe, (cost + is_obstacle, pos))

        raise Exception("Unreachable Code")