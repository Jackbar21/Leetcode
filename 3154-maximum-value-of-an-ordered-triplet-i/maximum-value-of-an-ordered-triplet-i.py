class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # return max(0, max(((nums[i] - nums[j]) * nums[k]) for i in range(len(nums)) for j in range(i + 1, len(nums)) for k in range(j + 1, len(nums))))
        # N = len(nums)
        # res = 0
        # for i in range(N):
        #     for j in range(i + 1, N):
        #         for k in range(j + 1, N):
        #             val = (nums[i] - nums[j]) * nums[k]
        #             if res < val:
        #                 res = val
        # return res
        self.nums = nums
        return self.dp(0, 1, 2)

    @cache
    def dp(self, i, j, k):
        nums = self.nums
        if i >= j:
            return self.dp(i, i + 1, k)
        
        if j >= k:
            return self.dp(i, j, j + 1)
        
        if k >= len(self.nums):
            return 0
        
        res = (nums[i] - nums[j]) * nums[k]
        return max(
            res,
            self.dp(i + 1, j, k),
            self.dp(i, j + 1, k),
            self.dp(i, j, k + 1)
        )
