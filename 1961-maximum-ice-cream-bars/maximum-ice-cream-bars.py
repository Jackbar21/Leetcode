class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res = 0
        heapq.heapify(costs)
        while costs and (coins := coins - heapq.heappop(costs)) >= 0:
            res += 1
        return res
        