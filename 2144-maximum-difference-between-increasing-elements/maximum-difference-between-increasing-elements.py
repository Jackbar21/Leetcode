class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        min_num = float("inf")
        for i, num in enumerate(nums):
            if num < min_num:
                min_num = num
            
            diff = num - min_num
            if res < diff:
                res = diff
        
        return res if res > 0 else -1