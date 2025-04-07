class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            # Sum is odd, 100% CANNOT partition it into two equal subsets in sum!
            return False
        
        self.nums = nums
        target_sum = sum_nums // 2
        return self.dp(0, target_sum)
    
    @cache
    def dp(self, i, sum_left):
        if sum_left <= 0 or i >= len(self.nums):
            return sum_left == 0
        
        num = self.nums[i]

        # Case 1: Include num
        case1 = self.dp(i + 1, sum_left - num)
        if case1:
            return True

        # Case 2: Don't include num
        case2 = self.dp(i + 1, sum_left)
        if case2:
            return True

        return False