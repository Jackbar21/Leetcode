class Solution:
    def findScore(self, nums: List[int]) -> int:
        # unmarked = set(range(len(nums)))
        marked = set()
        min_heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(min_heap)
        score = 0
        while len(min_heap) > 0:
            num, i = heapq.heappop(min_heap)
            if i in marked:
                continue
            score += num
            # unmarked.remove(i)
            # unmarked.discard(i - 1)
            # unmarked.discard(i + 1)
            marked.add(i - 1)
            marked.add(i)
            marked.add(i + 1)

            
        return score

        