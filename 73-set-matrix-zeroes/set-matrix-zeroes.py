class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0])

        # Idea: In order to use constant space, whenever a 0 is detected, set ALL of the values
        # in that row & column to some impossible value such as 'None'. This is because even something
        # as simple as tracking the row & column INDICES that need to be set to 0s will require O(M + N)
        # space!
        for row_index in range(M):
            for col_index in range(N):
                if matrix[row_index][col_index] != 0:
                    continue
                
                # This makes runtime no longer O(mn) tho :/
                for i in range(M):
                    if matrix[i][col_index] != 0:
                        matrix[i][col_index] = None
                for j in range(N):
                    if matrix[row_index][j] != 0:
                        matrix[row_index][j] = None
        
        for row_index in range(M):
            for col_index in range(N):
                if matrix[row_index][col_index] == None:
                    matrix[row_index][col_index] = 0
        
        return matrix