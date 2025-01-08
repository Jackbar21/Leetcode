class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        LEFT, RIGHT, UP, DOWN = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        DIRECTIONS = [LEFT, DOWN, RIGHT, UP]
        M, N = len(grid), len(grid[0])
        WATER, LAND = 0, 1

        max_area = 0
        # visited = set()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == WATER:
                    continue
                
                area = 0
                queue = collections.deque()
                queue.append((i, j))
                # visited.add((i, j))
                grid[i][j] = WATER
                while len(queue) > 0:
                    x, y = queue.popleft()
                    area += 1

                    for dx, dy in DIRECTIONS:
                        new_x, new_y = x + dx, y + dy
                        if (0 <= new_x < M and 
                            0 <= new_y < N and 
                            grid[new_x][new_y] == LAND #and 
                            # (new_x, new_y) not in visited
                        ):
                            # visited.add((new_x, new_y))
                            grid[new_x][new_y] = WATER
                            queue.append((new_x, new_y))
                
                if area > max_area:
                    max_area = area
        
        return max_area