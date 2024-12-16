class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(min_heap)

        for _ in range(k):
            num, index = heapq.heappop(min_heap)
            nums[index] *= multiplier
            heapq.heappush(min_heap, (num * multiplier, index))
        
        return nums