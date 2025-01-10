class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        X, O = "X", "O"
        M, N = len(board), len(board[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        global_visited = set()
        for i in range(M):
            for j in range(N):
                if board[i][j] == X or (i, j) in global_visited:
                    continue
                
                # Idea: Visit the island of O's in its entirety. If NONE of them
                # are on the boarder, then it must mean that they are COMPLETELY
                # surrounded by X's! Hence, we keep track of an 'is_surrounded'
                # variable that we initialize to True, and set to False if we
                # ever encounter an O on the boarder.
                # Need to keep track of visited Os in local visited set in case
                # we need to mark them all as X later on, before adding to global set.
                visited = set([(i, j)])
                queue = collections.deque([(i, j)])
                is_surrounded = True
                while len(queue) > 0:
                    x, y = queue.popleft()

                    # Check if (x, y) is on the border!
                    if x == 0 or x == M - 1 or y == 0 or y == N - 1:
                        is_surrounded = False

                    for dx, dy in DIRECTIONS:
                        neigh_x, neigh_y = x + dx, y + dy
                        if (0 <= neigh_x < M and 0 <= neigh_y < N
                            and board[neigh_x][neigh_y] == O
                            and (neigh_x, neigh_y) not in visited
                        ):
                            visited.add((neigh_x, neigh_y))
                            queue.append((neigh_x, neigh_y))
                
                if is_surrounded:
                    for x, y in visited:
                        board[x][y] = X
                global_visited = global_visited.union(visited)

