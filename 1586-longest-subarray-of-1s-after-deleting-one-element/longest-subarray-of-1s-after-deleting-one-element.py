class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # TOP-DOWN DP
        # self.nums = nums
        # self.memo = {}
        # return max(self.dp(i, True) for i in range(len(nums)))

        # BOTTOM-UP DP
        N = len(nums)
        dp = [[0, 0] for _ in range(N)] # dp[i][can_delete]
        res = 0
        if nums[N - 1] == 1:
            dp[N - 1][False] = 1
        for i in range(N - 2, -1, -1):
            num = nums[i]
            for can_delete in [True, False]:
                length = (
                    1 + dp[i + 1][can_delete] if num == 1 else
                    dp[i + 1][False] if can_delete == True else
                    0
                )
                dp[i][can_delete] = length
                if res < length and can_delete:
                    res = length
        return res
            
    
    def dp(self, i, can_delete):
        if (i, can_delete) in self.memo:
            return self.memo[(i, can_delete)]
        nums = self.nums
        N = len(nums)
        
        assert i < N
        if i == N - 1:
            res = int(nums[i] == 1 and can_delete == False)
            self.memo[(i, can_delete)] = res
            return res
        
        if nums[i] == 1:
            res = 1 + self.dp(i + 1, can_delete)
            self.memo[(i, can_delete)] = res
            return res
        
        if can_delete:
            res = self.dp(i + 1, False)
            self.memo[(i, can_delete)] = res
            return res
        
        res = 0
        self.memo[(i, can_delete)] = res
        return res
