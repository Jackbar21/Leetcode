class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        period = 0
        prev_price = float("inf")
        res = len(prices)
        for price in prices:
            if prev_price == price + 1:
                period += 1
            else:
                res += period * (period + 1) // 2
                period = 0

            prev_price = price

        return res + period * (period + 1) // 2
