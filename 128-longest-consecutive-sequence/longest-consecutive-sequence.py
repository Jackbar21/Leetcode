class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        sorted_nums = sorted(set(nums))
        
        longest = 0
        cur = 1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                cur += 1
            else:
                longest = max(longest, cur)
                cur = 1
        
        return max(longest, cur)