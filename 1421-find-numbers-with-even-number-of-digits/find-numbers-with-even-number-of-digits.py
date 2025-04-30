class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(map(lambda num: len(str(num)) % 2 == 0, nums))