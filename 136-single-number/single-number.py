class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_num = 0
        for num in nums:
            xor_num ^= num
        return xor_num
