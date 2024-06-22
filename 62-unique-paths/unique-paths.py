class Solution:
    def __init__(self):
        self.memo = {}
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 1 and n <= 1:
            return 1
        
        if m <= 1 or n <= 1:
            return 1
        
        if (m, n) in self.memo:
            return self.memo[(m, n)]
        
        # Case 1: robot moved right
        # moving right 1 means n += 1
        case1 = self.uniquePaths(m, n - 1)

        # Case 2: robot moved down
        # moving down 1 means m += 1
        case2 = self.uniquePaths(m - 1, n)

        self.memo[(m, n)] = case1 + case2
        return self.memo[(m, n)]