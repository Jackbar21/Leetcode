class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        self.xor_total = 0

        def backtrack(i):
            if i >= len(nums):
                self.res += self.xor_total
                return
            
            num = nums[i]

            # Case 1: Include element at index i
            self.xor_total ^= num
            backtrack(i + 1)
            self.xor_total ^= num # Undo the xor, which can be done by xor'ing again!

            # Case 2: Don't include element at index i
            backtrack(i + 1)
        
        backtrack(0)
        return self.res
