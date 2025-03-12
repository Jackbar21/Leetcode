class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos, neg = 0, 0
        for num in nums:
            pos += num > 0
            neg += num < 0
        return pos if pos > neg else neg