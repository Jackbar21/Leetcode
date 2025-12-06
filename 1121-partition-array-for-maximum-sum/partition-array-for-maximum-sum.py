class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.nums, self.k, self.memo = arr, k, {}
        return self.dp(0)
    
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]

        nums, k = self.nums, self.k
        N = len(nums)

        nums_left = N - i
        if nums_left <= k:
            res = max(nums[i:]) * nums_left
            self.memo[i] = res
            return res
        
        # Can pick any num elements in range [1..k]
        res = float("-inf")
        max_num = float("-inf")
        for length in range(1, k + 1):
            num = nums[i + length - 1]
            if num > max_num:
                max_num = num
            
            res = max(res, length * max_num + self.dp(i + length))

        self.memo[i] = res
        return res
