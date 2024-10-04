class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cheapest_index = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[cheapest_index]:
                cheapest_index = i
            else:
                res = max(res, prices[i] - prices[cheapest_index])

        return res