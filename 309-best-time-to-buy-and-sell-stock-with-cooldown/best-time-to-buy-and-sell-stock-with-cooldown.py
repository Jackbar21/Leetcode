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

        # Case 1: Buy or Sell the stock
        #   Must SELL stock if have stock, in which case we skip by two days 
        #   and gain a profit of 'price', or must BUY stock if have no stock!
        res = self.dp(i + 2, False) + price if have_stock else self.dp(i + 1, True) - price
        
        # Case 2: Don't buy or sell the stock
        case2 = self.dp(i + 1, have_stock)

        if case2 > res:
            res = case2
        self.memo[(i, have_stock)] = res
        return res
