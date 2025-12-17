class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        self.prices, self.memo = prices, {}
        return self.dp(0, k, False, True)
    
    def dp(self, i, k, is_holding, is_normal):
        if (i, k, is_holding, is_normal) in self.memo:
            return self.memo[(i, k, is_holding, is_normal)]

        prices = self.prices
        N = len(prices)

        if i >= N:
            return 0 if not is_holding else float("-inf")
        
        if k == 0:
            return 0
        
        # Case 1: Ignore today
        case1 = self.dp(i + 1, k, is_holding, is_normal)

        # Case 2: is_holding=True, let's sell/buy
        case2 = float("-inf")
        if is_holding:
            sign = -1 if is_normal else 1
            case2 = sign * prices[i] + self.dp(i + 1, k - 1, False, True)
        
        # Case 3: Buy today
        case3 = float("-inf")
        if not is_holding:
            case3 = prices[i] + self.dp(i + 1, k, True, True)
        
        # Case 4: Short today
        case4 = float("-inf")
        if not is_holding:
            case4 = -prices[i] + self.dp(i + 1, k, True, False)

        res = max(case1, case2, case3, case4)
        self.memo[(i, k, is_holding, is_normal)] = res
        return res
