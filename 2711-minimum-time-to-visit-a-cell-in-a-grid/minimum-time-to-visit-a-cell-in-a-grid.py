class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            # Impossible problem! This is the ONLY case where the problem is impossible!
            return -1

        m, n = len(grid), len(grid[0])
        GOAL_STATE = (m - 1, n - 1)
        START_POSITION = (0, 0)

        visited = set([START_POSITION])
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        fringe = [(0, START_POSITION)] # (time, pos)
        # fringe = [] # (time, position, prev-position)
        # if grid[0][1] <= 1:
        #     fringe.append(1, (0, 1), START_POSITION)
        # if grid[1][0] <= 1:
        #     fringe.append(1, (1, 0), START_POSITION)
        # assert len(fringe) > 0

        # visited = set([START_POSITION])

        res = float("inf")
        while len(fringe) > 0:
            cur_time, (x, y) = heapq.heappop(fringe)
            time = cur_time + 1
            if (x, y) == GOAL_STATE:
                # res = min(res, cur_time)
                # print(f"{res=}")
                return cur_time
            
            # if (x, y) in visited:
            #     continue
            # visited.add((x, y))
            
            neighbors = []
            for dx, dy in DIRECTIONS:
                r, c = (x + dx, y + dy)

                # Check if out of bounds
                if r < 0 or r >= m or c < 0 or c >= n:
                    continue
                
                # Check if already visited
                if (r, c) in visited:
                    continue
                
                # If I can't "pay" to go to a cell UP FRONT, I can zig-zap
                # between the previous position and my current position, OVER AND OVER
                # AND OVER, stalling 2 seconds every time I go to the previous position and back,
                # until I'm "rich enough" in time to proceed to that cell. It is VERY important
                # to denote I pay 2 seconds at a time however!
                diff = grid[r][c] - time
                if diff <= 0:
                    # neighbors.append((r, c))
                    heapq.heappush(fringe, (time, (r, c)))
                    visited.add((r, c))
                else:
                    # Must be multiple of 2, since can only waste 2 seconds at a time!
                    if diff % 2 == 1:
                        diff += 1
                    heapq.heappush(fringe, (time + diff, (r, c)))
                    visited.add((r, c))
                    
                # if grid[r][c] <= cur_time + 1 and (r, c) not in visited:
                #     neighbors.append((r, c))
            
            # If a node is not the goal state and has no neighbors it can reach,
            # it is still possible for this node to be reached at a later time when
            # it CAN reach some of its neighbors! So if a node currently has no neighbors
            # it can reach, kindly remove it from the visited set, and continue onwards!
            # if len(neighbors) == 0:
            #     assert (x, y) in visited
            #     visited.remove((x, y))
            #     continue
            
            # for (r, c) in neighbors:
            #     heapq.heappush(fringe, (cur_time + 1, (r, c)))
            #     visited.add((r, c))


            
            # for dx, dy in DIRECTIONS:
            #     x, y = (pos_x + dx, pos_y + dy)
            #     if x < 0 or x >= m or y < 0 or y >= n:
            #         continue
            #     if grid[x][y] <= time and (x, y) not in visited:
            #         heapq.heappush(fringe, (time, (x, y)))
            #         visited.add((x, y))
        
        raise Exception("Unreachable Code!")
        return -1 if res == float("inf") else res
