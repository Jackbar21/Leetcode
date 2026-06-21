class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return sum(1 for coin in sorted(costs) if (coins := coins - coin) >= 0)
        