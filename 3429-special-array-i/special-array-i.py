class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all(nums[i - 1] % 2 != nums[i] % 2 for i in range(1, len(nums)))