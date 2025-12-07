class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        self.matrix, self.memo = matrix, {}
        self.DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.inBounds = lambda i, j: 0 <= i < M and 0 <= j < N
        return max(self.dp(i, j) for i in range(M) for j in range(N))
    
    def dp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        val = self.matrix[i][j]
        res = 1 # Current cell only
        for di, dj in self.DIRECTIONS:
            neigh_i, neigh_j = i + di, j + dj
            if not self.inBounds(neigh_i, neigh_j):
                continue

            if self.matrix[neigh_i][neigh_j] > val:
                case = 1 + self.dp(neigh_i, neigh_j)
                if case > res:
                    res = case
        
        self.memo[(i, j)] = res
        return res
