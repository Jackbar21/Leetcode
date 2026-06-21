class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res = 0
        heapq.heapify(costs)
        while costs and (val := heapq.heappop(costs)) <= coins:
            coins -= val
            res += 1
        return res