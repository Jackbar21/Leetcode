class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:

        # Base Case: if k == 0, then beauty is just current beauty in nums! 
        # We can do a simple sliding window search to figure that out :)
        # if k == 0:
        #     res = 1
        #     l = 0
        #     cur_num = nums[0]
        #     for r in range(len(nums)):
        #         if nums[r] == cur_num:
        #             continue
                
        #         # Otherwise, we have that only nums[l..r-1] is "beautiful". 
        #         res = max(res, r - l)
        #         l = r

        #     return max(res, len(nums) - l)

        # Idea: Now that I realize this problem is asking for SUBSEQUENCE and not SUBARRAY,
        # this becomes a lot more intuitive :) This problem SCREAMS to me DP, but while I was
        # trying to come up with a solution for SUBARRAY version, one idea that came natural to
        # me was recognizing each number in nums as an interval (of length 2k+1 each!), and
        # then sorting the elements to apply a "line sweep" algorithm idea. I was turned away from
        # this idea, until I realize that since this is a SUBSEQUENCE problem, there is NO ISSUE
        # AT ALL in sorted the elements!

        # Step 1: convert nums into intervals!

        intervals = []
        lower, upper = float("inf"), float("-inf") # global interval bounds!

        normal_scalar = min(nums) - k
        for num in nums:
            left, right = num - k, num + k
            intervals.append((left - normal_scalar, right - normal_scalar))
            # if left < lower:
            #     lower = left
            # if right > upper:
            #     upper = right

        START, END = 0, 1
        intervals.sort(key = lambda interval: interval[END])

        length = max(nums) + k - normal_scalar + 1
        line_sweep = [[0, 0] for _ in range(length)] # (start, end)
        for start, end in intervals:
            line_sweep[start][START] += 1
            line_sweep[end][END] += 1
        
        # print(f"{intervals=}")
        # print(f"{line_sweep=}")

        res = 0
        cur_overlap = 0
        for start, end in line_sweep:
            cur_overlap += start
            if cur_overlap > res:
                res = cur_overlap
            cur_overlap -= end

            # print(f"{start=}, {end=}, {cur_overlap=}, {res=}")

        return res