class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        M, N = len(grid), len(grid[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        inBounds = lambda x, y: 0 <= x < M and 0 <= y < N

        # Keep track of number of FRESH oranges, and for each rotten orange
        # update how long it takes to rot an orange. Note that this value should
        # be updated to always reflect the MINIMUM amount of time it takes to rot
        # an orange, i.e. if two rotten oranges can reach a fresh orange, the time
        # to rot the orange should be the minimum from the two rotten oranges distances.
        fresh_oranges_count = 0
        orange_to_time = {}
        for i in range(M):
            for j in range(N):
                cell = grid[i][j]
                if cell != ROTTEN:
                    fresh_oranges_count += (cell == FRESH)
                    continue
                
                # From this rotten orange, explore all possible "neighbors"
                queue = collections.deque([(i, j, 0)]) # (x, y, time/cost)
                visited = set([(i, j)])
                while len(queue) > 0:
                    x, y, time = queue.popleft()

                    for dx, dy in DIRECTIONS:
                        neigh_x, neigh_y = x + dx, y + dy
                        if (inBounds(neigh_x, neigh_y) 
                            and grid[neigh_x][neigh_y] == FRESH # TODO: Use walrus operator hehe
                            and (neigh_x, neigh_y) not in visited
                        ):
                            # It will take time + 1 seconds to rot this orange
                            # from the original rotten orange at grid[i][j].
                            orange_to_time[(neigh_x, neigh_y)] = min(
                                time + 1,
                                orange_to_time.get((neigh_x, neigh_y), float("inf"))
                            )
                            queue.append((neigh_x, neigh_y, time + 1))
                            visited.add((neigh_x, neigh_y))

        # Since there are already no fresh oranges at minute 0, the answer is just 0
        if fresh_oranges_count == 0:
            return 0

        rottable_oranges_count = len(orange_to_time)
        if rottable_oranges_count != fresh_oranges_count:
            # Not possible to rot ALL of the oranges!
            return -1
 
        return max(orange_to_time.values())
