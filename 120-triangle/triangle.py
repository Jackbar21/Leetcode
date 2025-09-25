class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.triangle = triangle
        return self.dp(0, 0)
    
    @cache
    def dp(self, i, j):
        triangle = self.triangle
        N = len(triangle)

        if i >= N:
            return 0
        
        val = self.triangle[i][j]
        
        case1 = val + self.dp(i + 1, j)
        case2 = val + self.dp(i + 1, j + 1)

        res = min(case1, case2)
        return res