class Solution:
    def findScore(self, nums: List[int]) -> int:
        unmarked = set(range(len(nums)))
        min_heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(min_heap)
        score = 0
        while len(unmarked) > 0:
            num, i = heapq.heappop(min_heap)
            if i not in unmarked:
                continue
            score += num
            unmarked.remove(i)
            unmarked.discard(i - 1)
            unmarked.discard(i + 1)
            
        return score

        