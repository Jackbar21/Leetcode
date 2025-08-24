class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        self.nums = nums
        return max(self.dp(i, True) for i in range(len(nums)))
    
    @cache
    def dp(self, i, can_delete):
        nums = self.nums
        N = len(nums)
        
        assert i < N
        if i == N - 1:
            return int(nums[i] == 1 and can_delete == False)
        
        if nums[i] == 1:
            return 1 + self.dp(i + 1, can_delete)
        
        if can_delete:
            return self.dp(i + 1, False)
        
        return 0
