class Solution:
    def knightDialer(self, n: int) -> int:
        self.MOD = pow(10, 9) + 7
        self.memo = {}
        actions_map = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        self.getActions = lambda digit: actions_map[digit]

        res = 0
        for digit in range(0, 9 + 1):
            res += self.dp(digit, n)
        return res % self.MOD
    
    @cache
    def dp(self, digit, n):
        if (digit, n) in self.memo:
            return self.memo[(digit, n)]

        # assert n >= 1
        if n == 1:
            return 1
        
        res = 0
        for new_digit in self.getActions(digit):
            res += self.dp(new_digit, n - 1)
        res %= self.MOD
        self.memo[(digit, n)] = res
        return res