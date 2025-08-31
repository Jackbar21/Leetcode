class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        row, col, square = defaultdict(set), defaultdict(set), defaultdict(set)
        for i in range(M):
            for j in range(N):
                if (digit := board[i][j]) != ".":
                    row[i].add(digit)
                    col[j].add(digit)
                    square[(i // 3, j // 3)].add(digit)

        self.is_complete = False
        def backtrack(i, j):
            if self.is_complete:
                return True

            if j >= N:
                j = 0
                i += 1
            
            if i >= M:
                self.is_complete = True
                return True
            
            if board[i][j] != ".":
                return backtrack(i, j + 1)
            
            for digit in "123456789":
                # If adding doesn't violate rules, try it & backtrack!
                if (
                    digit not in row[i] and
                    digit not in col[j] and
                    digit not in square[(i // 3, j // 3)]
                ):
                    board[i][j] = digit
                    row[i].add(digit)
                    col[j].add(digit)
                    square[(i // 3, j // 3)].add(digit)

                    if backtrack(i, j + 1):
                        return True

                    board[i][j] = "."
                    row[i].remove(digit)
                    col[j].remove(digit)
                    square[(i // 3, j // 3)].remove(digit)
            
            return False
        
        assert backtrack(0, 0)
        # return board
        