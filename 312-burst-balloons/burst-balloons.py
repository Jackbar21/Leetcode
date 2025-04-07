class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        self.nums = nums
        N = len(nums)
        return self.dp(1, N - 2)

    @cache
    def dp(self, i, j):
        nums = self.nums

        left_val = nums[i - 1]
        right_val = nums[j + 1]
        # getVal = lambda index: left_val * nums[index] * right_val
        left_times_right_val = left_val * right_val
        getVal = lambda index: nums[index] * left_times_right_val

        if i >= j:
            return getVal(i) if i == j else 0
        
        # We assume index k will be LAST balloon to get popped!
        return max(
            self.dp(i, k - 1) + getVal(k) + self.dp(k + 1, j)
            for k in range(i, j + 1)
        )
