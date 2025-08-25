class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # We can uniquely map each position (i,j) to the (i+j)'th diagonal
        M, N = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                diagonals[i + j].append(mat[i][j])
        res = []
        for key in sorted(diagonals.keys()):
            res.extend(diagonals[key] if key % 2 == 0 else diagonals[key][::-1])
        return res