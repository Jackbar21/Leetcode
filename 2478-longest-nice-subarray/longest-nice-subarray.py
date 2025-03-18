class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        l = 0
        cur_sum = 0
        cur_streak = 0
        for r, num in enumerate(nums):
            if (cur_sum | num) == (cur_sum + num):
                # Valid case, continue building the window!
                cur_sum += num
                continue

            # Invalid case, slide window from the left until valid again!

            # Step 1: Update res
            if res < r - l:
                res = r - l

            # Step 2: Shrink window until valid
            while (cur_sum | num) != (cur_sum + num):
                cur_sum -= nums[l]
                l += 1
            
            # Step 3: Add num to now valid window :)
            cur_sum += num

        return max(res, r - l + 1)