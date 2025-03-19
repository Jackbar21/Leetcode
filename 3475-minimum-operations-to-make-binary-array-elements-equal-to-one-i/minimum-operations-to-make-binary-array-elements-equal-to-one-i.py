class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Algorithm: Whenever we see zero, perform a flip operation!
        # If we see a zero in last two elements of array, we return -1
        res = 0

        for i, bit in enumerate(nums):
            if bit == 1:
                continue
            
            # assert bit == 0
            if i >= len(nums) - 2:
                return -1
            
            nums[i + 1] ^= 1
            nums[i + 2] ^= 1
            res += 1
        
        return res