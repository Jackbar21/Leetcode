class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low, sell high
        # up to the i'th day, keep track of the CHEAPEST found stock price so far.
        # then, update your maximum profit to the larger between currently found
        # maximum profit, and today's stock price - the cheapest stock price found so far.
        max_profit = 0
        cheapest_price = prices[0]
        for price in prices:
            if cheapest_price > price:
                cheapest_price = price
            else:
                max_profit = max(max_profit, price - cheapest_price)

        return max_profit