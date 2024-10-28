class Solution:
    def __init__(self):
        self.nums = None # hashset of nums!
        self.memo = {}
    def longestSquareStreak(self, nums: List[int]) -> int:
        self.nums = set(nums)

        max_streak = 0
        for num in nums:
            streak = self.getSquareStreakFromNum(num)
            max_streak = max(max_streak, streak)
        
        return max_streak if max_streak >= 2 else -1
    
    def getSquareStreakFromNum(self, num):
        if num in self.memo:
            return self.memo[num]
        
        next_square = pow(num, 2)
        res = 1 + self.getSquareStreakFromNum(next_square) if next_square in self.nums else 1
        self.memo[num] = res
        return res