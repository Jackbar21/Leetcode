class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        min_heap = [(-num, index) for index, num in enumerate(nums)]
        heapq.heapify(min_heap)
        res = []
        for _ in range(k):
            num, index = heapq.heappop(min_heap)
            res.append((-num, index))
        
        NUM, INDEX = 0, 1
        res.sort(key = lambda pair: pair[INDEX])
        return [pair[NUM] for pair in res]
