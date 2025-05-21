class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0])

        top_left_commands = set()

        for i in range(M):
            for j in range(N):
                num = matrix[i][j]
                if num == 0:
                    # matrix[i][j] = None
                    matrix[i][0] = None
                    # matrix[i][-1] = None
                    matrix[0][j] = None
                    # matrix[-1][j] = None

                    if i == 0:
                        top_left_commands.add("R")
                    if j == 0:
                        top_left_commands.add("C")
        
        for row in matrix:
            print(row)
        
        # for i in range(M):
        #     for j in range(N):
        #         num = matrix[i][j]
        #         if num == None:
        #             matrix[i][j] = 0

        # Handle first row (zero columns!)
        for j in range(1, N):
            if matrix[0][j] is None:
                for i in range(M):
                    if matrix[i][j] is not None:
                        matrix[i][j] = 0

        # Handle first column (zero rows!)
        for i in range(1, M):
            if matrix[i][0] is None:
                for j in range(N):
                    if matrix[i][j] is not None:
                        matrix[i][j] = 0
        
        # Wipe top row!
        if "R" in top_left_commands:
            for j in range(N):
                matrix[0][j] = 0
        
        # Wipe first col!
        if "C" in top_left_commands:
            for i in range(M):
                matrix[i][0] = 0
        


        print(f"\nPRE-CLEANUP:\n")
        for row in matrix:
            print(row)

        
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

#  N  N  3  N
#  N  0  7  8
#  N 10 11 12
#  N 14 15  0