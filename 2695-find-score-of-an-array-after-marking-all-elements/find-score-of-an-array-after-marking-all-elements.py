class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = set()
        min_heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(min_heap)
        score = 0
        while len(min_heap) > 0:
            num, i = heapq.heappop(min_heap)
            if i in marked:
                continue
            score += num
            for index in range(i - 1, i + 2):
                marked.add(index)
            # marked.add(i)
            # marked.add(i - 1)
            # marked.add(i + 1)
            
        return score

        