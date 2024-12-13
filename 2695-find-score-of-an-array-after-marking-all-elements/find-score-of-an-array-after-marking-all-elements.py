class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = set()
        min_heap = [(num, i) for i, num in enumerate(nums)]

        NUM, INDEX = 0, 1
        sorted_nums = sorted(min_heap)
        marked = set()
        score = 0
        i = 0
        N = len(sorted_nums)
        for num, i in sorted_nums:
            if i in marked:
                continue
            
            # Add the value of the chosen integer to score
            score += num
            
            # Mark the chosen element and its two adjacent elements if they exist
            marked.add(i - 1)
            marked.add(i)
            marked.add(i + 1)

        return score
            
            

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

        