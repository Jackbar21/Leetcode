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
        res = 0
        cur_amount = amount
        while cur_amount >= 0:
            res += self.dp(i + 1, cur_amount)
            cur_amount -= coin

        self.memo[(i, amount)] = res
        return res