class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # return self.setZeroesLinearSpace(matrix)    # O(M * N) time, O(M + N) space
        return self.setZeroesConstantSpace(matrix) # O((M * N)^2) time, O(1) space
    
    def setZeroesLinearSpace(self, matrix):
        M, N = len(matrix), len(matrix[0])

        # O(M + N) space!
        row_indices = set()
        col_indices = set()

        # O(M * N)
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    row_indices.add(i)
                    col_indices.add(j)
        
        # O(M * N)
        for row_index in row_indices:
            for col_index in range(N):
                matrix[row_index][col_index] = 0
        
        # O(M * N)
        for col_index in col_indices:
            for row_index in range(M):
                matrix[row_index][col_index] = 0
        
        return matrix

    
    def setZeroesConstantSpace(self, matrix: List[List[int]]) -> None:
        M, N = len(matrix), len(matrix[0])

        # Idea: In order to use constant space, whenever a 0 is detected, set ALL of the values
        # in that row & column to some impossible value such as 'None'. This is because even something
        # as simple as tracking the row & column INDICES that need to be set to 0s will require O(M + N)
        # space!
        # N.B. Any found 0 should NOT be set to None so that it can be looped over in the future so
        # that its column and row related values also become None or 0 later on!
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