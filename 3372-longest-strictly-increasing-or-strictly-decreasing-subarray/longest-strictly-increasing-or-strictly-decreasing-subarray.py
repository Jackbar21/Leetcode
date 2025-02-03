class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        # Find largest strictly increasing/decreasing subarray from index i, for 0 <= i < N
        for i in range(N):
            # Get longest increasing
            index = i
            while index + 1 < N and nums[index] < nums[index + 1]:
                index += 1
            length = index - i + 1
            if res < length:
                res = length

            # Get longest decreasing
            index = i
            while index + 1 < N and nums[index] > nums[index + 1]:
                index += 1
            length = index - i + 1
            if res < length:
                res = length

        return res
