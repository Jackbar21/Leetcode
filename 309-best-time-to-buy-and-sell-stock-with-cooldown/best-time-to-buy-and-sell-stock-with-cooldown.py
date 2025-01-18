class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices, self.memo = prices, {}
        return self.dp(0, False)
    
    def dp(self, i, have_stock):
        if (i, have_stock) in self.memo:
            return self.memo[(i, have_stock)]
        
        # No more transactions left, return 0 profit!
        if i >= len(self.prices):
            return 0
        
        price = self.prices[i]

        # Case 1: Buy the stock (can only do so if DON'T have stock!)
        # case1 = self.dp(i + 1, True) - price if not have_stock else 0
        
        # Case 2: Sell the stock (can only do so if DO have stock!)
        # Remember, cannot sell on next day, so augment i by TWO instead of ONE!
        # case2 = self.dp(i + 2, False) + price if have_stock else 0

        res = self.dp(i + 2, False) + price if have_stock else self.dp(i + 1, True) - price
        
        # Case 3: Do nothing (don't buy or sell)!
        case3 = self.dp(i + 1, have_stock)
        if case3 > res:
            res = case3

        # res = max(case1, case2, case3)
        self.memo[(i, have_stock)] = res
        return res
