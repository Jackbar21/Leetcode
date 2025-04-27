class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(N - 2):
            first, second, third = nums[i], nums[i + 1], nums[i + 2]
            if (first + third) * 2 == second:
                res += 1
        return res