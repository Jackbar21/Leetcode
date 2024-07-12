class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        for i, num in enumerate(nums):
            total += num
            nums[i] = total   
        return nums