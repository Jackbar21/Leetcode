class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_num = 0
        for num in range(len(nums) + 1):
            xor_num ^= num
        
        for num in nums:
            xor_num ^= num
        
        return xor_num