class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        cur_max = float("-inf")
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            cur_max = max(cur_max, prices[r] - prices[l])
        return cur_max