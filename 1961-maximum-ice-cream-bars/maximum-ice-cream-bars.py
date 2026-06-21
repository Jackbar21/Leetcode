class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res = 0
        heapq.heapify(costs)
        while costs and costs[0] <= coins:
            coins -= heapq.heappop(costs)
            res += 1
        return res
        