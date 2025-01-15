class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = {}
        self.dp(0)
        return max(max_val for _, max_val in self.memo.values())
        res = float("-inf")
        for i in range(len(nums)):
            _, max_val = self.dp(i)
            if res < max_val:
                res = max_val
        return res

    # dp(i) == maximum product subarray starting at index i
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]
        
        # Base Case: If at last index, can only pick that number for product!
        if i == len(self.nums) - 1:
            val = self.nums[i]
            self.memo[i] = (val, val)
            return (val, val)
        
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