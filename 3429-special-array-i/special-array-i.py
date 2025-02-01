class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev_parity = None
        for num in nums:
            parity = num % 2
            if parity == prev_parity:
                return False
            prev_parity = parity
        return True