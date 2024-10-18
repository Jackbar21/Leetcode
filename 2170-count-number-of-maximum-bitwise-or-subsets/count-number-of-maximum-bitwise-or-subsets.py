class Solution:
    def __init__(self):
        self.memo = {}
        self.max_bitwise_or = 0
        self.nums = None
    
    def countDp(self, i, bitwise_or):
        if (i, bitwise_or) in self.memo:
            return self.memo[(i, bitwise_or)]

        if i >= len(self.nums):
            return bitwise_or == self.max_bitwise_or

        # Case 1: Don't include index i
        case1 = self.countDp(i + 1, bitwise_or)
        
        # Case 2: Include index i
        case2 = self.countDp(i + 1, bitwise_or | self.nums[i])

        self.memo[(i, bitwise_or)] = case1 + case2
        return case1 + case2


    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Max bitwise or can simply be precomputed as bitwise or
        # of all the numbers in nums!
        max_bitwise_or = 0
        for num in nums:
            max_bitwise_or |= num

        # Since all numbers have value >= 1, and empty-set solutions are invalid,
        # there exist no plausible solutions, hence 0 is returned.
        if max_bitwise_or == 0:
            return 0
        
        self.nums = nums
        self.max_bitwise_or = max_bitwise_or
        return self.countDp(0, 0)