class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.BUY, self.SELL, self.COOLDOWN = 0, 1, 2
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
        case1 = float("-inf")
        if not have_stock:
            case1 = self.dp(i + 1, True) - price
        
        # Case 2: Sell the stock (can only do so if DO have stock!)
        # Remember, cannot sell on next day, so augment i by TWO instead of ONE!
        case2 = float("-inf")
        if have_stock:
            case2 = self.dp(i + 2, False) + price
        
        # Case 3: Do nothing (don't buy or sell)!
        case3 = self.dp(i + 1, have_stock)

        res = max(case1, case2, case3)
        self.memo[(i, have_stock)] = res
        return res

        # Case 2: Sell only, now cannot buy on next day!
        case2 = float("-inf") 
        if num_stock > 0: 
            case2 = self.dp(i + 2, num_stock - 1) + price
        
        res = max(case1, case2)
        for sell_stock in range(1, num_stock + 1):
            case = price * sell_stock + self.dp(i + 2, num_stock - sell_stock)
            res = max(res, case)
        
        # Case 3: Buy and Sell
        # case3 = self.dp(i + 2, num_stock)

        # res = max(case1, case2, case3)
        self.memo[(i, num_stock)] = res
        return res


        
        # Case 1: Buy the stock
        purchase_cost = self.prices[i]
        case1 = self.dp(i + 1, )

        # Case 3: BOTH buy the stock AND sell the stock!
        
        # Case 1: Choose to BUY the stock! Can ONLY do so if 'prev_action' was NOT SELL!
        case1 = float("-inf")
        if prev_action != self.SELL:
            buy_cost = self.prices[i]
            case1 = self.dp(i + 1, self.BUY, num_stock + 1) - buy_cost
        
        # Case 2: Choose to SELL the stock! Can ONLY do so if 'num_stock' > 0!
        case2 = float("-inf")
        if num_stock > 0:
            sell_profit = self.prices[i]
            case2 = self.dp(i + 1, self.SELL, num_stock - 1) + sell_profit
        
        # Case 3: Choose to go on cooldown! Can only do so if did a sell last turn maybe?
        case3 = float("-inf")
        if prev_action == self.SELL:
            case3 = self.dp(i + 1, self.COOLDOWN, num_stock)

        res = max(case1, case2, case3)
        self.memo[(i, prev_action, num_stock)] = res
        return res
