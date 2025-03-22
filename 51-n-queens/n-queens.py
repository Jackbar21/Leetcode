class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Rows: use row index (e.g. i, 0 <= i < n)
        # Columns: use col index (e.g. j, 0 <= j < n)
        # Negative Diagonals: use col - row index (e.g. j - i)
        # Positive Diagonals: use row + col

        # Already used up indices!
        # rows = set() # Can ignore!
        cols = set()
        neg_diags = set()
        pos_diags = set()

        # There will only be one queen per row, so might as well backtrack through row indices!
        arr = [["."] * n for _ in range(n)]
        #print(f"{arr=}")
        def backtrack(i):
            #print(f"{i=}, {arr=}")
            if i == n:
                yield list("".join(row) for row in arr)
                return


            for j in range(n):
                if j in cols or (j - i) in neg_diags or (i + j) in pos_diags:
                    continue
                
                # Prepare add
                cols.add(j)
                neg_diags.add(j - i)
                pos_diags.add(i + j)
                assert arr[i][j] == "."
                arr[i][j] = "Q"

                # Get more solutions
                yield from backtrack(i + 1)

                # Undo (for backtracking!)
                assert arr[i][j] == "Q"
                arr[i][j] = "."
                cols.remove(j)
                neg_diags.remove(j - i)
                pos_diags.remove(i + j)

        
        res = list(backtrack(0))
        #print(f"{res=}")
        return res


        
        

