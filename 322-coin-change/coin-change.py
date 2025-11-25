class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        res = self.dp(0, amount)
        return res if res != float("inf") else -1
    
    @cache
    def dp(self, i, amount_left):
        coins = self.coins
        N = len(coins)

        if amount_left < 0:
            return float("inf")

        if i >= N:
            return 0 if amount_left == 0 else float("inf")
        
        # Case 1: Pick coins[i]
        case1 = 1 + self.dp(i, amount_left - coins[i])

        # Case 2: Skip coins[i]
        case2 = self.dp(i + 1, amount_left)

        return min(case1, case2)