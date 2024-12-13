class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = set()
        sorted_nums = sorted((num, i) for i, num in enumerate(nums))
        score = 0
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
