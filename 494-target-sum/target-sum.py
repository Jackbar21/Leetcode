class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        self.memo = {}
        return self.dp(0, 0)
    
    # @cache
    def dp(self, i, cur_sum):
        if (i, cur_sum) in self.memo:
            return self.memo[(i, cur_sum)]
    
        if i >= len(self.nums):
            return cur_sum == self.target
        
        num = self.nums[i]

        # Case 1: Add a '+' before num
        case1 = self.dp(i + 1, cur_sum + num)

        # Case 2: Add a '-' before num
        case2 = self.dp(i + 1, cur_sum - num)
    
        res = case1 + case2
        self.memo[(i, cur_sum)] = res
        return res