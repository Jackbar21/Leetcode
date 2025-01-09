class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M, N = len(heights), len(heights[0])
        RIGHT, DOWN, LEFT, UP = (0, 1), (1, 0), (0, -1), (-1, 0)
        DIRECTIONS = [RIGHT, DOWN, LEFT, UP]
        inBounds = lambda x, y: 0 <= x < M and 0 <= y < N
        
        def bfs(queue):
            visited = set(queue)

            while len(queue) > 0:
                x, y = queue.popleft()
                height = heights[x][y]

                for dx, dy in DIRECTIONS:
                    neigh_x, neigh_y = x + dx, y + dy

                    if (inBounds(neigh_x, neigh_y)
                        and (neigh_x, neigh_y) not in visited
                        and heights[neigh_x][neigh_y] >= height # INVERTING the problem!
                    ):
                        visited.add((neigh_x, neigh_y))
                        queue.append((neigh_x, neigh_y))

            return visited

        pacific_queue = collections.deque()
        atlantic_queue = collections.deque()
        for i in range(M):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, N - 1))
        for j in range(N):
            pacific_queue.append((0, j))
            atlantic_queue.append((M - 1, j))

        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        return list(pacific_reachable.intersection(atlantic_reachable))
