class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = l = r = 0
        for num in nums:
            if num != 0:
                l = r + 1
            else:
                res += r - l + 1
            r += 1
        return res
