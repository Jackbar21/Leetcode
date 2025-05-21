class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
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
