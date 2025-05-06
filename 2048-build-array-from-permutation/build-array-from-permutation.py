class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return list(map(lambda index: nums[nums[index]], range(len(nums))))