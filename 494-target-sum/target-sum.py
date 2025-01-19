class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # self.nums, self.target, self.memo = nums, target, {}
        # return self.dp(0, 0)
        N = len(nums)
        sum_nums = sum(nums)
        max_target = sum_nums
        min_target = -sum_nums
        TARGET_RANGE = max_target - min_target

        if not (min_target <= target <= max_target):
            return 0

        def sumToIndex(cur_sum):
            return cur_sum + sum_nums
        
        def indexToSum(index):
            return index - sum_nums

        dp = [[0] * (TARGET_RANGE + 1) for _ in range(N + 1)]
        dp[N][sumToIndex(target)] = 1

        for i in range(N - 1, -1, -1):
            num = nums[i]
            for cur_sum in range(min_target + num, max_target + 1 - num):
            # for cur_sum in range(TARGET_RANGE):
                # dp[i][cur_sum] = 
                # val = 0
                cur_sum_index = sumToIndex(cur_sum)

                new_sum = cur_sum + num
                new_sum_index = sumToIndex(new_sum)
                if 0 <= new_sum_index <= TARGET_RANGE:
                    # if cur_sum + num <= max_target:
                    dp[i][cur_sum_index] += dp[i + 1][new_sum_index]

                new_sum = cur_sum - num
                new_sum_index = sumToIndex(new_sum)
                if 0 <= new_sum_index <= TARGET_RANGE:
                    # if cur_sum + num <= max_target:
                    dp[i][cur_sum_index] += dp[i + 1][new_sum_index]
        
        return dp[0][sumToIndex(0)]

    
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
