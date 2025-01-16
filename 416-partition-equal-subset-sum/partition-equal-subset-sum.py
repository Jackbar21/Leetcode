class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Idea: to partition nums into two subsets of equal sum, they must each be
        # exactly HALF of the sum of ALL the numbers in nums. Trivially, if the sum is
        # odd, the answer is immediately False as the sum cannot be divided into two in the
        # first place! Otherwise, this problem is essentially Subset Sum, where the target
        # is sum(nums)/2. But this would be a pseudopolynomial time algorithm, so something
        # BETTER we can do is for each index i in nums, ADD it to our current sum if we choose
        # to put it in the FIRST subset, or otherwise SUBTRACT it if we choose to put it in the
        # SECOND subset! That way, if we reach a final sum of 0, we know it's because the sums
        # of the first and second subsets are EQUAL.
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        target = sum_nums // 2
        nums.sort()
        self.nums, self.memo = nums, {}
        return self.dp2d(0, target)


    def dp2d(self, i, target):
        if (i, target) in self.memo:
            return self.memo[(i, target)]
        
        if i >= len(self.nums):
            return target == 0
        
        # Since numbers cannot be negative, we know answer is False
        # immediately if target < 0
        if target < 0:
            return False
        
        num = self.nums[i]

        # Case 1: Include num in subset
        case1 = self.dp2d(i + 1, target - num)

        # Case 2: Don't include num in subset
        case2 = self.dp2d(i + 1, target)

        res = case1 or case2
        self.memo[(i, target)] = res
        return res