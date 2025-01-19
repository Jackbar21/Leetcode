class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums, self.target, self.memo = nums, target, {}
        return self.dp(0, 0)

    
    def dp(self, i, cur_sum):
        if (i, cur_sum) in self.memo:
            return self.memo[(i, cur_sum)]

        # Base Case: Made a choice for every single digit in nums,
        # so return 1 to indiciate it is a valid expression if and only
        # if the cur_sum is equal to the original target. Otherwise, return
        # 0, as it is NOT a valid expression.
        if i >= len(self.nums):
            return cur_sum == self.target
        
        num = self.nums[i]

        # Case 1: Add a '+' in front of num
        case1 = self.dp(i + 1, cur_sum + num)

        # Case 2: Add a '-' in front of num
        case2 = self.dp(i + 1, cur_sum - num)

        res = case1 + case2
        self.memo[(i, cur_sum)] = res
        return res
