class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        l = 0
        res = 0
        for r, num in enumerate(nums):
            if num != 0:
                l = r + 1
                continue
            
            res += r - l + 1
        
        return res
