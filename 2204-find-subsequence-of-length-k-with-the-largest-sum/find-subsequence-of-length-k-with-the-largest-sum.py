class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        NUM, INDEX = 0, 1
        max_heap = [(-num, index) for index, num in enumerate(nums)]
        heapq.heapify(max_heap)

        res = [heapq.heappop(max_heap) for _ in range(k)]
        res.sort(key = lambda pair: pair[INDEX])
        return [-pair[NUM] for pair in res]
