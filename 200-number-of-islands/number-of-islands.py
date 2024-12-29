class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        WATER, LAND = "0", "1"
        M, N = len(grid), len(grid[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def inBounds(x, y):
            return 0 <= x < M and 0 <= y < N

        visited = set()
        num_islands = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == WATER or (i, j) in visited:
                    continue
                
                # Here, we have at least one unvisited Land Cell, so we must
                # augment the total number of islands found, as well as mark
                # every adjacent/reachable island-cell from this current position
                # as visited (since they are all part of the SAME island)
                num_islands += 1
                queue = collections.deque([(i, j)]) # bfs
                visited.add((i, j))
                while len(queue) > 0:
                    x, y = queue.popleft()

                    for dx, dy in DIRECTIONS:
                        neigh_x, neigh_y = x + dx, y + dy

                        if (inBounds(neigh_x, neigh_y) and
                            grid[neigh_x][neigh_y] == LAND and
                            (neigh_x, neigh_y) not in visited
                        ):
                            visited.add((neigh_x, neigh_y))
                            queue.append((neigh_x, neigh_y))

        return num_islands
