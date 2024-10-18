class Solution:
    def __init__(self):
        self.memo = {}
        self.max_bitwise_or = 0
        self.nums = None
    def getBitwiseOr(self, nums):
        bitwise_or = 0
        for num in nums:
            bitwise_or |= num
        return bitwise_or
    
    def backtrack(self, i, bitwise_or):
        if i >= len(self.nums):
            return bitwise_or == self.max_bitwise_or
        
        count = 0
        # Case 1: Include index i
        count += self.backtrack(i + 1, bitwise_or | self.nums[i])

        # Case 2: Don't include index i
        count += self.backtrack(i + 1, bitwise_or)

        return count


    def countDp(self, i, bitwise_or):
        if (i, bitwise_or) in self.memo:
            return self.memo[(i, bitwise_or)]
        
        print(f"{i=}, {self.nums=}")
        if i >= len(self.nums):
            return 0
        
        res = 0

        # Case 1: Include i
        case1, bitwise_or1 = self.countDp(i + 1, bitwise_or | self.nums[i])
        if bitwise_or1 == self.max_bitwise_or:
            res += case1

        # Case 2: Don't include i
        case2, bitwise_or2 = self.countDp(i + 1, bitwise_or)
        if bitwise_or2 == self.max_bitwise_or:
            res += case2
        
        self.memo[(i, bitwise_or)] = res
        return res
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # max_bitwise_or = 0
        # for num in nums:
        #     max_bitwise_or |= num
        max_bitwise_or = self.getBitwiseOr(nums)
        if max_bitwise_or == 0:
            return 0
        
        self.nums = nums
        self.max_bitwise_or = max_bitwise_or
        return self.backtrack(0, 0)
        return self.countDp(0, 0)
        count = 0
        d = {nums[0]: 1}
        for i in range(1, len(nums)):
            bitwise_or = self.getBitwiseOr(d.keys())
            count += bitwise_or == max_bitwise_or

            # Loop Invariant
            d[nums[i - 1]] -= 1
            if d[nums[i - 1]] == 0:
                del d[nums[i - 1]]
            
            d[nums[i]] = d.get(nums[i], 0) + 1

        print(d, self.getBitwiseOr(d.keys()), max_bitwise_or)
        return count
        return max_bitwise_or