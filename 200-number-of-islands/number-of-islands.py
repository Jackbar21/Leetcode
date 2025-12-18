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

                queue = deque([(i, j)])
                visited.add((i, j))
                
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in DIRECTIONS:
                        nx, ny = x + dx, y + dy
                        if inBounds(nx, ny) and (nx, ny) not in visited and grid[nx][ny] == LAND:
                            queue.append((nx, ny))
                            visited.add((nx, ny))
                
                res += 1
        
        return res
