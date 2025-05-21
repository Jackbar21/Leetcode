class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(1) extra space solution!
        M, N = len(matrix), len(matrix[0])
        clear_first_row, clear_first_col = False, False

        for i in range(M):
            for j in range(N):
                num = matrix[i][j]
                if num == 0:
                    matrix[i][0] = None
                    matrix[0][j] = None

                    if i == 0:
                        clear_first_row = True
                    if j == 0:
                        clear_first_col = True

        # Handle first row (zero columns!)
        for j in range(1, N):
            if matrix[0][j] is None:
                for i in range(M):
                    matrix[i][j] = 0

        # Handle first column (zero rows!)
        for i in range(1, M):
            if matrix[i][0] is None:
                for j in range(N):
                    matrix[i][j] = 0
        
        # Wipe top row!
        if clear_first_row:
            for j in range(N):
                matrix[0][j] = 0
        
        # Wipe first col!
        if clear_first_col:
            for i in range(M):
                matrix[i][0] = 0
        
        # Cleanup!
        for i in range(M):
            for j in range(N):
                if matrix[i][j] is None:
                    matrix[i][j] = 0
        
        return matrix


        # O(M + N) space solution
        """
        M, N = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        for i in range(M):
            for j in range(N):
                num = matrix[i][j]
                if num == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        for i in range(M):
            for j in range(N):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
        
        return matrix
        """
