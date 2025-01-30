class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Idea: Flip the rows in matrix, then transpose matrix!
        N = len(matrix)

        # Step 1: Transpose the matrix (can only modify matrix)
        for i in range(N):
            for j in range(i + 1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Flip the rows in matrix (can only modify matrix)
        for i in range(N):
            l, r = 0, N - 1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1

        return
