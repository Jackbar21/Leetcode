class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(num-nums[i-1]) for i, num in enumerate(nums))