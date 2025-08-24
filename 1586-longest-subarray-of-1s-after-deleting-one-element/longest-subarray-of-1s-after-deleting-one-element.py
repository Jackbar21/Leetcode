class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = {}
        return max(self.dp(i, True) for i in range(len(nums)))
    
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
