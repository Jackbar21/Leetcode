class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        WATER, LAND = 0, "1"
        M, N = len(grid), len(grid[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # visited = set()
        num_islands = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] != LAND: # or (i, j) in visited:
                    continue
                
                # Here, we have at least one unvisited Land Cell, so we must
                # augment the total number of islands found, as well as mark
                # every adjacent/reachable island-cell from this current position
                # as visited (since they are all part of the SAME island)
                num_islands += 1
                fringe = [(i, j)] # dfs
                # visited.add((i, j))
                grid[i][j] = WATER
                while len(fringe) > 0:
                    x, y = fringe.pop()

                    for dx, dy in DIRECTIONS:
                        neigh_x, neigh_y = x + dx, y + dy

                        if (0 <= neigh_x < M and 0 <= neigh_y < N and
                            grid[neigh_x][neigh_y] == LAND #and
                            # (neigh_x, neigh_y) not in visited

                        ):
                            # visited.add((neigh_x, neigh_y))
                            grid[neigh_x][neigh_y] = WATER
                            fringe.append((neigh_x, neigh_y))

        return num_islands