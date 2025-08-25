class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # We can uniquely map each position (i,j) to the (i+j)'th diagonal
        M, N = len(mat), len(mat[0])
        diagonals = [[] for _ in range(M + N - 1)]
        for i in range(M):
            for j in range(N):
                diagonals[i + j].append(mat[i][j])
        res = []
        for i, diagonal in enumerate(diagonals):
            res.extend(diagonal if i % 2 == 1 else diagonal[::-1])
        return res