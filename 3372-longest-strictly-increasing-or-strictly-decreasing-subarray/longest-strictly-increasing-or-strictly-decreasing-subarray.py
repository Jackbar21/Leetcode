class Solution:
    def longestIncreasingSlidingWindow(self, nums):
        # Constraints say all nums are >= 1, so prev_num == 0 for intial value works!
        res, count, prev_num = 0, 0, 0 
        for num in nums:
            if prev_num < num:
                count += 1
                prev_num = num
                continue
            
            if res < count:
                res = count
            count = 1
            prev_num = num
        
        return res if res > count else count
    
    def longestDecreasingSlidingWindow(self, nums):
        return self.longestIncreasingSlidingWindow(reversed(nums))

    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest_increasing = self.longestIncreasingSlidingWindow(nums)
        longest_decreasing = self.longestDecreasingSlidingWindow(nums)
        return longest_increasing if longest_increasing > longest_decreasing else longest_decreasing
