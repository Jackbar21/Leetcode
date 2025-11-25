class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.memo = {}
        res = self.dp(0, amount)
        return res if res != float("inf") else -1
    
    def dp(self, i, amount_left):
        if (i, amount_left) in self.memo:
            return self.memo[(i, amount_left)]

        coins = self.coins
        N = len(coins)

        if amount_left < 0:
            return float("inf")
        elif amount_left == 0:
            return 0
        elif i >= N:
            return float("inf")
        
        # Case 1: Pick coins[i]
        case1 = 1 + self.dp(i, amount_left - coins[i])

        # Case 2: Skip coins[i]
        case2 = self.dp(i + 1, amount_left)

        res = case1 if case1 < case2 else case2
        self.memo[(i, amount_left)] = res
        return res