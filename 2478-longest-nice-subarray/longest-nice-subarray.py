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

            # Invalid case, must RESTART the window
            # WRONG: Shift the window until valid again!

            # Step 1: Update res
            # assert r - l + 1 == cur_streak
            assert (cur_sum | num) < (cur_sum + num)
            # # print(f"{l=}, {r=}, {r-l+1=}, {cur_streak=}")
            res = max(res, r - l)

            # Step 2: Shrink window until valid
            # # print(f"before: {l,r,prev_num,num,nums[l:r+1]=}")
            while (cur_sum | num) != (cur_sum + num):
                # # print(f"{l,r,cur_sum,num=}")
                cur_sum -= nums[l]
                l += 1
            cur_sum += num
            # print(f"FINAL: {l,r,cur_sum,num=}")

        return max(res, r - l + 1)