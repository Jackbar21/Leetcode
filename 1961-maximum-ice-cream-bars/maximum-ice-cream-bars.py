class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i, cost in enumerate(costs):
            if coins < cost:
                return i
            coins -= cost
        return i + 1