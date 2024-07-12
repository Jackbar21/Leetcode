class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            nums[i] = total   
        return nums