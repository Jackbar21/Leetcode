class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        for row in range(m):
            for col in range(n):
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]

            curr_row = sorted(matrix[row], reverse=True)
            for i in range(n):
                ans = max(ans, curr_row[i] * (i + 1))

        return ans

# class Solution:
#     def largestSubmatrix(self, matrix: List[List[int]]) -> int:
#         M, N = len(matrix), len(matrix[0])
#         matrix = [[1] * (c := row.count(1)) + [0] * (len(row) - c) for row in matrix]
#         self.counts = [row.count(1) for row in matrix]
#         self.matrix = matrix

#         res = 0
#         for i in range(M):
#             length, height = self.dp(i)
#             res = max(res, length * height)
#         return res

#         return max(self.dp(i) for i in range(M))
    
#     @cache
#     def dp(self, i):
#         # Returns (length, height)
#         matrix = self.matrix
#         counts = self.counts
#         M, N = len(matrix), len(matrix[0])

#         if i == M - 1:
#             return (counts[i], 1)

#         # Starting from matrix[i][0] as our top left corner
#         l, h = self.dp(i + 1)
#         c = counts[i]

#         return (min(l, c), h + 1)

