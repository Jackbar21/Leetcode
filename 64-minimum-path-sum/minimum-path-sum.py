class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid
        return self.dp(0, 0)
    
    @cache
    def dp(self, i, j):
        grid = self.grid
        M, N = len(grid), len(grid[0])

        if i >= M or j >= N:
            return float("inf")

        cost = grid[i][j]
        if i == M - 1 and j == N - 1:
            return cost
        
        # Case 1: Move Right
        case1 = cost + self.dp(i, j + 1)

        # Case 2: Move Down
        case2 = cost + self.dp(i + 1, j)

        return min(case1, case2)
