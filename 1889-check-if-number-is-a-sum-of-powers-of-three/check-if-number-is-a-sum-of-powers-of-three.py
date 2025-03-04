class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # max_expo = math.floor(math.log(n, 3))
        # for expo in range(max_expo, -1, -1):
        #     n -= pow(3, expo)
            # if self.dp(n):
        
        return self.dp(n, 1)

    @cache
    def dp(self, n, expo):
        if n <= 0:
            return n == 0
        
        if expo >= n:
            return expo == n
        
        next_expo = expo * 3
        return self.dp(n - expo, next_expo) or self.dp(n, next_expo)
