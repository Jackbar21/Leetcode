class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # Let's list all the possible powers of x that we are able to choose from. Since n >= 1 and x >= 1, the minimum
        # base will simply be 1 as 1^x will always be 1.
        self.MOD = pow(10, 9) + 7
        self.x = x
        self.memo = {}
        return self.dp(n, 1) % self.MOD
    
    def dp(self, n, base):
        if (n, base) in self.memo:
            return self.memo[(n, base)]
        x = self.x
        exp = pow(base, x)
        # assert exp > 0 and n >= 0

        if n == 0:
            return 1

        if exp > n:
            return 0
        
        # Case 1: Include exp
        case1 = self.dp(n - exp, base + 1) # Cannot use same base again, since must be **unique** positive integers

        # Case 2: Don't include exp
        case2 = self.dp(n, base + 1) # Move on to next base

        res = case1 + case2
        self.memo[(n, base)] = res
        return res
