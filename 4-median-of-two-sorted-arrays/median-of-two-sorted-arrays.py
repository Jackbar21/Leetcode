class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        N = len(nums)
        if N % 2 == 1:
            return nums[N // 2]
        return (nums[N // 2] + nums[-1 + N // 2]) / 2