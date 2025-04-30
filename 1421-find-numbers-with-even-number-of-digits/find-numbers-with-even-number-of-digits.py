class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len(nums) - sum(map(lambda num: len(str(num)) & 1, nums))