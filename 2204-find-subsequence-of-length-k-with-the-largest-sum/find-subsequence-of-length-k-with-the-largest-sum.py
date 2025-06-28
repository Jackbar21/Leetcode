class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heapq.heapify(max_heap := [(-num, index) for index, num in enumerate(nums)]);return [-num for num, _ in sorted((heapq.heappop(max_heap) for _ in range(k)), key = lambda pair: pair[1])]