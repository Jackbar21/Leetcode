class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M, N = len(heights), len(heights[0])
        RIGHT, DOWN, LEFT, UP = (0, 1), (1, 0), (0, -1), (-1, 0)
        DIRECTIONS = [RIGHT, DOWN, LEFT, UP]
        inBounds = lambda x, y: 0 <= x < M and 0 <= y < N

        # Populate all the cells that can reach the Pacific Ocean
        # First, we know all the cells where i == 0 or j == 0 will yield 'True'
        # Then we want to do all the cells where i == 1 or j == 1, then i == 2 or j == 2
        res = set()
        for i in range(M):
            for j in range(N):
                # Do a BFS traversal and keep track of whenever a border-square is reached
                # (indicating that an ocean can be reach)
                reach_pacific, reach_atlantic = False, False
                queue = collections.deque([(i, j)])
                visited = set([(i, j)])
                while len(queue) > 0:
                    x, y = queue.popleft()

                    if x == 0 or y == 0:
                        reach_pacific = True
                    
                    if x == M - 1 or y == N - 1:
                        reach_atlantic = True

                    if reach_pacific and reach_atlantic:
                        res.add((i, j))
                        break
                    
                    height = heights[x][y]
                    for dx, dy in DIRECTIONS:
                        neigh_x, neigh_y = x + dx, y + dy

                        if (inBounds(neigh_x, neigh_y)
                            and (neigh_x, neigh_y) not in visited
                            and heights[neigh_x][neigh_y] <= height
                        ):
                            visited.add((neigh_x, neigh_y))
                            queue.append((neigh_x, neigh_y))
        
        return list(res)
                    

