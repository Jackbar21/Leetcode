class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l = res = 0
        for r, num in enumerate(nums):
            if num == 0:
                res += r - l + 1
            else:
                l = r + 1
        return res