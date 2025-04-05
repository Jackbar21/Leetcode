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
        # Backtrack solution, O(2^N), where N = len(nums)
        self.nums = nums
        self.res = 0
        self.xor_total = 0
        self.backtrack(0)
        return self.res
