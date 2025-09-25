class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.triangle, self.memo = triangle, {}
        return self.dp(0, 0)
    
    def dp(self, i, j):
        triangle, memo = self.triangle, self.memo

        if (i, j) in memo:
            return memo[(i, j)]

        N = len(triangle)
        if i >= N:
            return 0
        
        val = self.triangle[i][j]

        case1 = val + self.dp(i + 1, j)
        case2 = val + self.dp(i + 1, j + 1)

        res = case1 if case1 < case2 else case2
        memo[(i, j)] = res
        return res