class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        max_heap = [(-num, index) for index, num in enumerate(nums)]
        heapq.heapify(max_heap) # O(N)
        res = []
        for _ in range(k):
            num, index = heapq.heappop(max_heap)
            res.append((-num, index))
        
        NUM, INDEX = 0, 1
        res.sort(key = lambda pair: pair[INDEX])
        return [pair[NUM] for pair in res]
