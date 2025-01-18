class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.m, self.n, self.memo = m, n, {}
        return self.dp(0, 0)
    
    def dp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        M, N = self.m, self.n
        if i == M - 1 and j == N - 1:
            return 1
        
        # Case 1: Move down, can only do so if i + 1 < m (otherwise, 0 moves!)
        case1 = self.dp(i + 1, j) if i + 1 < M else 0

        # Case 2: Move right, can only do so if j + 1 < n (otherwise, 0 moves!)
        case2 = self.dp(i, j + 1) if j + 1 < N else 0

        res = case1 + case2
        self.memo[(i, j)] = res
        return res
