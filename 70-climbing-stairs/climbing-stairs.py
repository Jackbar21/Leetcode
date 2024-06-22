class Solution:
    def __init__(self):
        self.memo = {}
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        if n not in self.memo:
            v1 = 0 + self.climbStairs(n - 1)
            v2 = 0 + self.climbStairs(n - 2)
            self.memo[n] = v1 + v2

        return self.memo[n]
        
        
        