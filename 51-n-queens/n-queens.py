class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Suppose we want to insert a queen at index (i, j)
        # Rows: use row index (e.g. i, 0 <= i < n)
        # Columns: use col index (e.g. j, 0 <= j < n)
        # Negative Diagonals: use col - row index (e.g. j - i)
        # Positive Diagonals: use row + col (e.g. i + j)
        res = []

        # Already used up indices!
        # rows = set() # Can ignore!
        cols = set()
        neg_diags = set()
        pos_diags = set()

        # There will only be one queen per row, so might as well backtrack through row indices!
        board = [["."] * n for _ in range(n)]
        def backtrack(i):
            if i == n:
                res.append(list("".join(row) for row in board))
                return

            for j in range(n):
                col_index = j
                neg_diag_index = j - i
                pos_diag_index = i + j
                if (
                    col_index in cols
                    or neg_diag_index in neg_diags
                    or pos_diag_index in pos_diags
                ):
                    continue
                
                # Prepare add
                cols.add(col_index)
                neg_diags.add(neg_diag_index)
                pos_diags.add(pos_diag_index)
                board[i][j] = "Q"

                # Get more solutions
                backtrack(i + 1)

                # Undo (for backtracking!)
                board[i][j] = "."
                cols.remove(col_index)
                neg_diags.remove(neg_diag_index)
                pos_diags.remove(pos_diag_index)

        
        backtrack(0)
        return res
