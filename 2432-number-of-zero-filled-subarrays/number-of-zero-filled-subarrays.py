class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = l = 0
        for r, num in enumerate(nums):
            if num != 0:
                l = r + 1
            else:
                res += r - l + 1
        return res
