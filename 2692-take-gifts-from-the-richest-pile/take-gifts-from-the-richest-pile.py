class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = list(map(lambda num: -num, gifts)) # max heap!
        heapq.heapify(max_heap) 
        res = 0
        for _ in range(k):
            max_pile = -heapq.heappop(max_heap)
            leave_behind = math.floor(math.sqrt(max_pile))
            heapq.heappush(max_heap, -leave_behind)
        return -sum(max_heap)