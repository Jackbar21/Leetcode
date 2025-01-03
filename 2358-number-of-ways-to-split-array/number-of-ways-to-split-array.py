class Solution:
    def getSubarraySum(self, i, j):
        return self.prefix_sums[j] - (self.prefix_sums[i - 1] if i > 0 else 0)

    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sums = [] # prefix_sums[i] == sum(nums[0..i])
        cur_sum = 0
        for num in nums:
            cur_sum += num
            prefix_sums.append(cur_sum)
        self.prefix_sums = prefix_sums
        nums_sum = cur_sum

        res = 0
        for i in range(len(nums) - 1):
            # split into nums[0..i] | nums[i+1..len(nums)-1]
            # to guarantee that there is at least one element to the right of i,
            # if must be that nums[i+1..len(nums)-1] is non-empty, further implying
            # that i+1 must be less-than-or-equal-to len(nums)-1, i.e. i <= len(nums) - 2
            # Hence, why we don't consider the case for i being len(nums) - 1 directly.
            # res += self.getSubarraySum(0, i) >= self.getSubarraySum(i + 1, len(nums) - 1)
            res += prefix_sums[i] >= nums_sum - (prefix_sums[i] if i+1 > 0 else 0)
        
        return res
