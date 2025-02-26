class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # Idea: We want largest absolute subarray sum. Why not get largest subarray sum, smallest 
        # subarray sum, and take the larger of the two values (absolute value'd of course)
        return max(
            self.maxSubarraySum(nums),
            abs(self.maxSubarraySum([-num for num in nums]))
        )
    
    def maxSubarraySum(self, nums):
        cur_sum = 0
        res = nums[0] # Default value
        for num in nums:
            cur_sum += num
            if res < cur_sum:
                res = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return res