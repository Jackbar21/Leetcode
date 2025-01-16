class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.memo = {}
        self.nums = nums
        return max(self.dp(i) for i in range(len(nums)))
    
    # dp(i) == length of LIS that STARTS at index i in nums
    # Time Complexity:
    #   - O(N) suproblems
    #   - O(N) time per suproblem
    #   == O(N^2) total time
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]
        
        nums = self.nums
        if i >= len(nums):
            return 0
        
        # We are starting the LIS at index i
        start_val = nums[i]
        res = 1 # Base Case: only take number at index i!

        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                new_case = 1 + self.dp(j)
                if res < new_case:
                    res = new_case
        
        self.memo[i] = res
        return res
