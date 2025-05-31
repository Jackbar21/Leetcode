class Solution:
    def getSquareCoordinates(self, square):
        board, N = self.board, self.N
        # assert 1 <= square <= pow(N, 2)

        row_index_backwards = (square // N) - (square % N == 0)
        row_index = (N - 1) - row_index_backwards

        # Column index gets affected by "Boustrophedon style", hence
        # need to check if base row index (i.e. 'row_index_backwards')
        # is odd or even!
        start_square_of_row = row_index_backwards * N + 1
        column_offset = square - start_square_of_row
        column_index = (
            column_offset
            if row_index_backwards % 2 == 0
            else N - column_offset - 1
        )

        return row_index, column_index

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        self.board, self.N = board, N
        N_SQUARED = pow(N, 2)
        GOAL_STATE = N_SQUARED
        fringe = collections.deque([(0, 1)]) # (cost, curr_square)
        best_cost = [float("inf")] * (N_SQUARED + 1)
        
        while fringe:
            cost, curr_square = fringe.popleft()

            if curr_square == GOAL_STATE:
                return cost
            
            if cost >= best_cost[curr_square]:
                continue
            best_cost[curr_square] = cost
            
            next_cost = cost + 1
            for next_square in range(curr_square + 1, min(curr_square + 6, GOAL_STATE) + 1):
                r, c = self.getSquareCoordinates(next_square)
                final_square = next_square if board[r][c] == -1 else board[r][c]
                fringe.append((next_cost, final_square))
        
        return -1
