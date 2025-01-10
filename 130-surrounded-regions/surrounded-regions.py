class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # return self.solveNaive(board)
        return self.solveEfficient(board)
    
    def solveEfficient(self, board: List[List[str]]) -> None:
        # As compared to solveNaive, we can leverage the fact
        # that only Os on the boarder can't be surrounded, and
        # effectively any Os neighboring those other border Os.
        # So, instead of looping through all M * N cells, we can
        # loop through the 4 borders for a total of 2M + 2N - 2 cells,
        # reducing the complexity of #-of-islands-calls to O(M + N) instead
        # of O(M * N). Then, for all remaining O's in the board, we will need
        # to mark them as X's since they are guaranteed to be surrounded.
        # Despite that taking O(M * N) time, this is still a better solution :)
        # Edit: Similar to "Pacific Atlantic Water Flow" problem, we can initialize
        # a queue with the border elements for only ONE total bfs call. Therefore,
        # this approach is MUCH DEFINITELY more efficient, as it makes it a HARD
        # O(M * N) worst case time complexity overall!
        X, O = "X", "O"
        M, N = len(board), len(board[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # Step 1: Iterate through the four borders, and add any Os found to the bfs-queue
        queue = collections.deque()
        for i in range(M):
            # Left Column
            if board[i][0] == O:
                queue.append((i, 0))

            # Right Column
            if board[i][N - 1] == O:
                queue.append((i, N - 1))
        
        for j in range(N):
            # Top Row
            if board[0][j] == O:
                queue.append((0, j))
            
            # Bottom Row
            if board[M - 1][j] == O:
                queue.append((M - 1, j))
        
        # Now, do a BFS from these Os on the boarder to find all neighboring
        # Os which are guaranteed to NOT be surrounded!
        visited = set(queue)
        while len(queue) > 0:
            x, y = queue.popleft()

            for dx, dy in DIRECTIONS:
                neigh_x, neigh_y = x + dx, y + dy
                neigh = (neigh_x, neigh_y)
                if (0 <= neigh_x < M and 0 <= neigh_y < N
                    and board[neigh_x][neigh_y] == O
                    and neigh not in visited
                ):
                    visited.add(neigh)
                    queue.append(neigh)
        
        # Now, we have access to ALL the Os that ARE NOT surrounded. We should now
        # traverse the entire board, and set any O that is NOT in this set (meaning it
        # IS surrounded) to an X.
        for i in range(M):
            for j in range(N):
                if board[i][j] == O and (i, j) not in visited:
                    board[i][j] = X
        
        # Don't return anything, i.e. only supposed to modify board in-place :)
        return

    def solveNaive(self, board: List[List[str]]) -> None:
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

        # Don't return anything, i.e. only supposed to modify board in-place :)
        return
