class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        self.memo = {}
        self.nums = nums

        return self.dp(0, 0)
    
    @cache
    def dp(self, i, needed_remainder):
        nums = self.nums
        N = len(nums)
        if i >= N:
            return 0 if needed_remainder == 0 else float("-inf")

        # Case 1: Skip nums[i]
        case1 = self.dp(i + 1, needed_remainder)

        # Case 2: Choose nums[i]
        num = nums[i]
        remainder = num % 3
        new_needed_remainder = needed_remainder - remainder
        if new_needed_remainder < 0:
            new_needed_remainder += 3
        case2 = num + self.dp(i + 1, new_needed_remainder)

        return max(case1, case2)
