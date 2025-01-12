class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = {}
        return self.dp(0, False)

    def dp(self, i, robbed_house_one):
        if (i, robbed_house_one) in self.memo:
            return self.memo[(i, robbed_house_one)]

        # Base Case: No more homes left to rob
        if i >= len(self.nums):
            return 0
        
        # Base Case 2: If we're at the last house, and chose to rob
        # the first house, we cannot rob this home!
        if i == len(self.nums) - 1 and robbed_house_one:
            return 0
        
        # Case 1: Rob house at index i
        case1 = self.nums[i] + self.dp(i + 2, robbed_house_one or i == 0)

        # Case 2: Don't rob house at index i
        case2 = 0 + self.dp(i + 1, robbed_house_one)

        res = max(case1, case2)
        self.memo[(i, robbed_house_one)] = res
        return res
        