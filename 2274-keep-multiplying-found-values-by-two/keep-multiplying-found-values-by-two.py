class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        unique = set(nums)
        while original in unique:
            original *= 2
        return original