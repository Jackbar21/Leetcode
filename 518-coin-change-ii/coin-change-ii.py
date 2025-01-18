class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.coins, self.memo = coins, {}
        return self.dp(0, amount)

    def dp(self, i, amount):
        if (i, amount) in self.memo:
            return self.memo[(i, amount)]
        
        if i >= len(self.coins):
            return amount == 0
        
        coin = self.coins[i]

        # Case 1: Use current coin (can only do so if doesn't bring you negative!)
        case1 = self.dp(i, amount - coin) if amount >= coin else 0

        # Case 2: Move on to next coin
        case2 = self.dp(i + 1, amount)

        res = case1 + case2
        self.memo[(i, amount)] = res
        return res
