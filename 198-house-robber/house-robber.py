class Solution:
    def __init__(self):
        self.memo = {}
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0] if len(nums) > 0 else 0
        
        n = len(nums)
        # Case 1: rob last home
        if (n - 2) not in self.memo:
            self.memo[n - 2] = self.rob(nums[:n - 2])
        case1 = nums[-1] + self.memo[n - 2]

        # Case 2: don't rob last home
        if (n - 1) not in self.memo:
            self.memo[n - 1] = self.rob(nums[:n - 1])
        case2 = self.memo[n - 1]

        return max(case1, case2)