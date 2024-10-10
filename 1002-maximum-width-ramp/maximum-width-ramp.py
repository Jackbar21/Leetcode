class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # pairs = []
        # for i in range(len(nums)):
        #     pairs.append((nums[i], i))
        
        # pairs.sort()
        pairs = sorted(range(len(nums)), key = lambda index: nums[index])
        res = 0
        min_index = float("inf")
        for index in pairs:
            min_index = min(min_index, index)
            res = max(res, index - min_index)
        
        return res
