class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        score = 0
        for _ in range(k):
            num = -heapq.heappop(max_heap)
            score += num
            heapq.heappush(max_heap, -math.ceil(num / 3))
        
        return score
