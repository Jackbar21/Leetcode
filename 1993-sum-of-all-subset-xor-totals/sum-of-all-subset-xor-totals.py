class Solution:
    def backtrack(self, i):
        nums = self.nums
        if i >= len(nums):
            self.res += self.xor_total
            return
        
        num = nums[i]

        # Case 1: Include element at index i
        self.xor_total ^= num
        self.backtrack(i + 1)
        self.xor_total ^= num # Undo the xor, which can be done by xor'ing again!

        # Case 2: Don't include element at index i
        self.backtrack(i + 1)

    def subsetXORSum(self, nums: List[int]) -> int:
        # Let N = len(nums)
        # Backtrack solution, O(2^N)
        self.nums = nums
        self.res = 0
        self.xor_total = 0
        self.backtrack(0)
        return self.res

        self.nums = nums
        return self.dp(0)

    @cache
    def dp(self, i):
        nums = self.nums
        N = len(nums)

        if i >= N:
            return 0
        
        num = nums[i]

        # Get sum of all XOR totals starting from nums[i+1:]
        rest_sum = self.dp(i + 1)

        case1 = num ^ rest_sum
        case2 = rest_sum

        return case1 + case2