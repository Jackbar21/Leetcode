class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        cur_num = 0
        for i, num in enumerate(nums):
            cur_num <<= 1
            cur_num |= num
            nums[i] = (cur_num % 5 == 0)
        return nums