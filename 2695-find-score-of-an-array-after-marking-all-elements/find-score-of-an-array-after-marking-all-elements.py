class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = set()
        min_heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(min_heap)
        score = 0
        while len(marked) < len(nums):
            num, i = heapq.heappop(min_heap)
            if i in marked:
                continue
            score += num
            marked.add(i)
            if i != 0:
                # unmarked.discard(i - 1)
                marked.add(i - 1)
            if i != len(nums) - 1:
                marked.add(i + 1)
            # unmarked.discard(i + 1)
            
        return score

        