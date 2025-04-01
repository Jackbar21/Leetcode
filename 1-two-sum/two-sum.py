class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            wanted_num = target - num
            if wanted_num in seen:
                return [seen[wanted_num], i]
            seen[num] = i
        raise Exception("No solution.")