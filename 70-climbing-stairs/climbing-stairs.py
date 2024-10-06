class Solution:
    def __init__(self):
        self.memo = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        return self.climbStairsDp(n)
    
    def climbStairsDp(self, i):
        if i in self.memo:
            return self.memo[i]
        
        self.memo[i] = self.climbStairsDp(i - 1) + self.climbStairsDp(i - 2)
        return self.memo[i]
        