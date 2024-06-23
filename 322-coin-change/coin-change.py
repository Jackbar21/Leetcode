class Solution:
    def __init__(self):
        self.memo = {}
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in self.memo:
            return self.memo[amount]
        
        if amount <= 0:
            return 0 if amount == 0 else -1
        
        res = float("inf")
        for coin in coins:
            if amount - coin >= 0:
                val = self.coinChange(coins, amount - coin)
                if val != -1:
                    res = min(res, val+1)
        
        if res == float("inf"):
            res = -1
        
        self.memo[amount] = res
        return res