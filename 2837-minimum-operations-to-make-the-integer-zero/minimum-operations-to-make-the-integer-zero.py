class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        k = 1
        while True:
            x = num1 - num2 * k
            if x < k:
                return -1
            if k >= x.bit_count():
                return k
            k += 1
    def makeTheIntegerZeroAttempt(self, num1: int, num2: int) -> int:
        self.num1, self.num2 = num1, num2
        res = self.dp(num1)
        return res if res != float("inf") else -1
    
    @cache
    def dp(self, num):
        if num < 0:
            return float("inf") # Infinite operations
        
        if num == 0:
            return 0
        
        res = float("inf")
        for i in range(60, -1, -1):
            if self.num2 + pow(2, i) >= 0:
                continue
            case = self.dp(num - self.num2 - pow(2, i))
            if res < case:
                res = case
        return res
