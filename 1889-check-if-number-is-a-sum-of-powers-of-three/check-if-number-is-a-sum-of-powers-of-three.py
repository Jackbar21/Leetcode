class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        self.memo = {}
        return self.dp(n, 1)

    def dp(self, n, expo):
        if (n, expo) in self.memo:
            return self.memo[(n, expo)]
        if n <= 0:
            return n == 0
        
        if expo >= n:
            return expo == n
        
        next_expo = expo * 3
        res = self.dp(n - expo, next_expo) or self.dp(n, next_expo)
        self.memo[(n, expo)] = res
        return res
