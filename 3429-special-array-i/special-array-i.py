class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        parity = lambda num: num % 2
        prev_num = nums[0] + 1
        for num in nums:
            if parity(prev_num) == parity(num):
                return False
            prev_num = num
        return True