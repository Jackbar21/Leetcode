class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        fringe = [(0, 0, 0)] # (time, x, y)
        N, M = len(moveTime), len(moveTime[0])
        GOAL_STATE = (N - 1, M - 1)
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        inBounds = lambda x, y: 0 <= x < N and 0 <= y < M

        # visited = set([(0, 0)])
        visited = set()
        while len(fringe) > 0:
            time, x, y = heapq.heappop(fringe)
            # assert (x, y) not in visited
            if (x, y) in visited:
                continue # Already saw this position with a BETTER time!
            visited.add((x, y))

            if (x, y) == GOAL_STATE:
                return time
            
            for dx, dy in DIRECTIONS:
                neigh_x, neigh_y = x + dx, y + dy
                if not inBounds(neigh_x, neigh_y):
                    continue
                if (neigh_x, neigh_y) in visited:
                    continue
                
                time_to_reach_neigh = max(time, moveTime[neigh_x][neigh_y]) + 1
                heapq.heappush(fringe, (time_to_reach_neigh, neigh_x, neigh_y))
                # visited.add((neigh_x, neigh_y))
        
        raise Exception("No solution found!")
