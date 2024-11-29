class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # The premise of my solution comes from the idea that if you're able to expand
        # onwards from the original square, you're ALWAYS able to traverse back and forth
        # from a previous & current position, stalling a total of 2 seconds at a time in doing
        # this, allowing one to traverse ANY square using this technique. Hence the ONLY possible
        # way for there NOT to be a solution in this problem, is if it isn't possible to traverse
        # a singular step forward from the original position.
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        m, n = len(grid), len(grid[0])
        GOAL_STATE = (m - 1, n - 1)
        START_POSITION = (0, 0)
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        fringe = [(0, START_POSITION)] # (time, pos)
        visited = set([START_POSITION])

        while True:
            cur_time, (x, y) = heapq.heappop(fringe)
            if (x, y) == GOAL_STATE:
                return cur_time
            
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
                time = cur_time + 1
                diff = grid[r][c] - time
                if diff > 0:
                    # Must be multiple of 2, since can only waste 2 seconds at a time!
                    time += diff + (diff % 2)

                heapq.heappush(fringe, (time, (r, c)))
                visited.add((r, c))
