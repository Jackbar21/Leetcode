class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = l = r = 0
        for num in nums:
            r += 1
            if num != 0:
                l = r
            res += r - l
        return res