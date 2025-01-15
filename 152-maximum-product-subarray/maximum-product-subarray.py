class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = {}
        res = float("-inf")
        for i in range(len(nums)):
            _, max_val = self.dp(i)
            res = max(res, max_val)
        return res

    # dp(i) == maximum product subarray starting at index i
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]
        
        # Base Case
        if i >= len(self.nums):
            # 1 multiplied by anything is 1, so make both min & max 1!
            return (1, 1)
        
        # Case 1: Only consider current element
        val = self.nums[i]
        min_val, max_val = self.dp(i + 1)

        new_min_val = min(
            val,
            min_val * val,
            max_val * val
        )

        new_max_val = max(
            val,
            min_val * val,
            max_val * val
        )

        res = (new_min_val, new_max_val)
        self.memo[i] = res
        return res