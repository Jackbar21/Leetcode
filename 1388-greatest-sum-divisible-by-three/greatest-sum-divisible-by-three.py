class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        self.memo = {}
        self.nums = nums

        return self.dp(0, 0)
    
    def dp(self, i, needed_remainder):
        if (i, needed_remainder) in self.memo:
            return self.memo[(i, needed_remainder)]
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

        res = max(case1, case2)
        self.memo[(i, needed_remainder)] = res
        return res