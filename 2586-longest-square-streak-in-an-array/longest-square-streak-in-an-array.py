class Solution:
    def __init__(self):
        self.nums = None # hashset of nums!
        self.memo = {}
    def longestSquareStreak(self, nums: List[int]) -> int:
        self.nums = set(nums)

        # We now know there exists at least one square streak, so max value is AT LEAST 1
        max_streak = 1

        for num in nums:
            streak = self.getSquareStreakFromNum(num)
            max_streak = max(max_streak, streak)
        
        return max_streak if max_streak > 1 else -1
    
    def getSquareStreakFromNum(self, num):
        if num in self.memo:
            return self.memo[num]
        
        next_square = pow(num, 2)
        if next_square not in self.nums:
            self.memo[num] = 1
            return 1
        
        res = 1 + self.getSquareStreakFromNum(next_square)
        self.memo[num] = res
        return res