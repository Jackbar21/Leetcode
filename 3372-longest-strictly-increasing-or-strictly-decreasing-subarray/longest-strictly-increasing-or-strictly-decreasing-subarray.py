class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        isSorted = lambda subarray: all(subarray[i - 1] < subarray[i] for i in range(1, len(subarray)))
        for i in range(N):
            for j in range(i, N):
                subarray = nums[i:j+1]
                if isSorted(subarray) or isSorted(subarray[::-1]):
                    res = max(res, len(subarray))
        return res