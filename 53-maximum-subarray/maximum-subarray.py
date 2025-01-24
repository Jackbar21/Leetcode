class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        cur_sum = 0
        max_sum = nums[0]
        for num in nums:
            cur_sum += num
            if cur_sum < 0:
                cur_sum = 0
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum