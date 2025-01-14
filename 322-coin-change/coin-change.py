class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins, self.memo = coins, {}
        res = self.dp(amount)
        return res if res != 99999 else -1
    
    def dp(self, amount_left):
        if amount_left in self.memo:
            return self.memo[amount_left]
        
        # Was able to reach the EXACT amount, so don't need ANY more coins!
        if amount_left == 0:
            return 0
        
        # If amount_left < 0, this means we "overshot" the amount (since we're working
        # backwards from the original amount down to 0), so we return that we need "infinity"
        # coins to make this solution path work, obviously discouraging this solution from
        # being chosen... as this is a minimization problem :)
        if amount_left < 0:
            return 99999
        
        res = 99999
        for coin in self.coins:
            res = min(res, 1 + self.dp(amount_left - coin))

        self.memo[amount_left] = res
        return res
