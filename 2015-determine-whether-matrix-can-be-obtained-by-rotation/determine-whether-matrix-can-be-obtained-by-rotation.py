class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if self.equalMatrix(mat, target):
                return True
            
            mat = self.rotateMatrix(mat)
        return False
    
    def rotateMatrix(self, matrix):
        M, N = len(matrix), len(matrix[0])
        res = [[-1] * N for _ in range(M)]

        for i in range(M):
            for j in range(N):
                res[i][j] = matrix[j][N - i - 1]
        
        return res
    
    def equalMatrix(self, matrix1, matrix2):
        M1, N1 = len(matrix1), len(matrix1[0])
        M2, N2 = len(matrix2), len(matrix2[0])

        return M1 == M2 and N1 == N2 and all(matrix1[i][j] == matrix2[i][j] for i in range(M1) for j in range(N1))