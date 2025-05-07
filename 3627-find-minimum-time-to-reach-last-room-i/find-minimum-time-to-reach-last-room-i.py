class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        N, M = len(moveTime), len(moveTime[0])
        GOAL_STATE = (N - 1, M - 1)
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        inBounds = lambda x, y: 0 <= x < N and 0 <= y < M

        visited = set()
        fringe = [(0, 0, 0)] # (time, x, y)
        while len(fringe) > 0:
            time, x, y = heapq.heappop(fringe)

            # If we've reached GOAL_STATE, we know we've reached
            # it w/ OPTIMAL time thanks to UCS!
            if (x, y) == GOAL_STATE:
                return time

            if (x, y) in visited:
                continue # Already saw this position with a BETTER time!
            visited.add((x, y))
            
            for dx, dy in DIRECTIONS:
                neigh_x, neigh_y = x + dx, y + dy
                if inBounds(neigh_x, neigh_y) and (neigh_x, neigh_y) not in visited:
                    time_to_reach_neigh = max(time, moveTime[neigh_x][neigh_y]) + 1
                    heapq.heappush(fringe, (time_to_reach_neigh, neigh_x, neigh_y))

        raise Exception("No solution found!")
