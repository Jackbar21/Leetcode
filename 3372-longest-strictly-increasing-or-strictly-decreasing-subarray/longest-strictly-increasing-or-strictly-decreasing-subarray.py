class Solution:
    def longestIncreasingSlidingWindow(self, nums):
        prev_num = float("-inf")
        res = 0
        count = 0
        for num in nums:
            if prev_num < num:
                count += 1
                prev_num = num
                continue
            
            res = max(res, count)
            count = 1
            prev_num = num
        
        return max(res, count)







    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        return max(
            self.longestIncreasingSlidingWindow(nums),      # longest strictly INCREASING subarray
            self.longestIncreasingSlidingWindow(nums[::-1]) # longest strictly DECREASING subarray
        )
        



        N = len(nums)
        res = 0
        # Find largest strictly increasing/decreasing subarray from index i, for 0 <= i < N
        for i in range(N):
            # Get longest increasing
            index = i
            while index + 1 < N and nums[index] < nums[index + 1]:
                index += 1
            length = index - i + 1
            if res < length:
                res = length

            # Get longest decreasing
            index = i
            while index + 1 < N and nums[index] > nums[index + 1]:
                index += 1
            length = index - i + 1
            if res < length:
                res = length

        return res
