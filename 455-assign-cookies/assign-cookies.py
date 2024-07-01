class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        heapq.heapify(g)
        heapq.heapify(s)

        res = 0
        while len(s) > 0 and len(g) > 0:
            smallest_cookie = heapq.heappop(s)
            if smallest_cookie >= g[0]:
                res += 1
                heapq.heappop(g)
        return res