class Solution:
    def __init__(self):
        self.memo = {} # (i, target), representing nums[:i+1]
        self.nums = None
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        return self.findTargetDp(len(nums)-1, target)
        
    def findTargetDp(self, i, target):
        # i == 0 <==> len(nums) == 1
        if i <= 0:
            # '-' or '+' in front of 0 doesn't affect value!
            if self.nums[0] == target == 0:
                return 2
            return 1 if abs(self.nums[0]) == abs(target) else 0
        if (i, target) in self.memo:
            return self.memo[(i, target)]
        # Number of ways for nums[:i+1]
        # is just two cases for slapping a
        # '+' or '-' for nums[i], and using
        # nums[:i] result recursively (with memoization)
        res = 0

        # Case 1: Slap a '+' for nums[i]
        res += self.findTargetDp(i - 1, target - self.nums[i])

        # Case 2: Slap a '-' for nums[i]
        res += self.findTargetDp(i - 1, target + self.nums[i])

        self.memo[(i, target)] = res
        return res
