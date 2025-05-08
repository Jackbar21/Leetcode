class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # Constants
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        N, M = len(moveTime), len(moveTime[0])
        GOAL_STATE = (N - 1, M - 1)

        # Helper Functions
        updateMoveCost = lambda move_cost: 1 if move_cost == 2 else 2
        inBounds = lambda x, y: 0 <= x < N and 0 <= y < M

        # Setup
        fringe = [(0, 1, 0, 0)] # (time, move_cost, x, y)
        visited = set()

        # Logic
        while fringe:
            time, move_cost, x, y = heapq.heappop(fringe)

            if (x, y) == GOAL_STATE:
                return time
            
            if (x, y) in visited:
                continue
            visited.add((x, y))

            for dx, dy in DIRECTIONS:
                neigh_x, neigh_y = x + dx, y + dy
                if not inBounds(neigh_x, neigh_y):
                    continue
                if (neigh_x, neigh_y) in visited:
                    continue

                neigh_cost = max(time, moveTime[neigh_x][neigh_y]) + move_cost
                heapq.heappush(fringe, (neigh_cost, updateMoveCost(move_cost), neigh_x, neigh_y))
        
        raise Exception("No Solution Found!")
