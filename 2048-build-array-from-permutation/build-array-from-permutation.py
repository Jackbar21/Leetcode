class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return list(nums[nums[index]] for index in range(len(nums)))