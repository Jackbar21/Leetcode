class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.nums = arr
        self.k = k
        return self.dp(0)
    
    @cache
    def dp(self, i):
        nums = self.nums
        k = self.k
        N = len(nums)

        nums_left = N - i
        if nums_left <= k:
            return max(nums[i:]) * nums_left
        
        # Can pick any num elements in range [1..k]
        res = float("-inf")
        max_num = float("-inf")
        for length in range(1, k + 1):
            num = nums[i + length - 1]
            if num > max_num:
                max_num = num
            
            res = max(res, length * max_num + self.dp(i + length))

        return res
