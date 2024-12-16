class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(min_heap)

        for _ in range(k):
            num, index = heapq.heappop(min_heap)
            heapq.heappush(min_heap, (num * multiplier, index))
        
        min_heap.sort(key = lambda tup: tup[1])
        return [tup[0] for tup in min_heap]