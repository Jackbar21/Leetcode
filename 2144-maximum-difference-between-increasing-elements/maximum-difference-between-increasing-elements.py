class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(N):
            num_i = nums[i]
            for j in range(i + 1, N):
                num_j = nums[j]
                diff = num_j - num_i
                if res < diff:
                    res = diff
        return res if res > 0 else -1