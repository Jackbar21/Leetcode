class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        WATER, LAND = "0", "1"
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        inBounds = lambda i, j: 0 <= i < M and 0 <= j < N
        visited = set()
        res = 0

        for i in range(M):
            for j in range(N):
                if grid[i][j] != LAND or (i, j) in visited:
                    continue

                stack = [(i, j)]
                visited.add((i, j))
                
                while stack:
                    x, y = stack.pop()
                    for dx, dy in DIRECTIONS:
                        nx, ny = x + dx, y + dy
                        if inBounds(nx, ny) and (nx, ny) not in visited and grid[nx][ny] == LAND:
                            stack.append((nx, ny))
                            visited.add((nx, ny))
                
                res += 1
        
        return res
