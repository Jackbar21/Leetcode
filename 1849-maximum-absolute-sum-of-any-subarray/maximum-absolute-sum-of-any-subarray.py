class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # N = len(nums)
        # prefix_sums = []
        # cur_sum = 0
        # for num in nums:
        #     cur_sum += num
        #     prefix_sums.append(cur_sum)
        
        # getSubarraySum = lambda i, j: prefix_sums[j] - (prefix_sums[i - 1] if i > 0 else 0)
        # return max(abs(getSubarraySum(i, j)) for i in range(N) for j in range(i, N))

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