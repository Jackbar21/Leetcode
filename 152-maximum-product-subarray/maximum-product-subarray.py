class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = {}
        res = float("-inf")
        for i in range(len(nums)):
            min_val, max_val = self.dp(i)
            print(f"{res=}, {min_val=}, {max_val=}")
            res = max(res, min_val, max_val)
        return res

    # dp(i) == maximum product subarray starting at index i
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]
        
        # Base Case
        if i == len(self.nums) - 1:
            # Only one number, so maximum "product" is number itself
            val = self.nums[i]
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

        # Case 1: 
        self.memo[i] = (new_min_val, new_max_val)
        return self.memo[i]