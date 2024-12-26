class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        return self.dp(0, 0)
    
    @cache
    def dp(self, i, cur_sum):
        if i >= len(self.nums):
            return int(cur_sum == self.target)
        
        num = self.nums[i]

        # Case 1: Add a '+' before num
        case1 = self.dp(i + 1, cur_sum + num)

        # Case 2: Add a '-' before num
        case2 = self.dp(i + 1, cur_sum - num)

        return case1 + case2