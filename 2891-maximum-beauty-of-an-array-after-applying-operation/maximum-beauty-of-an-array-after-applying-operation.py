class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        START, END = 0, 1
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
        intervals.sort(key = lambda interval: interval[END])

        # O(n + k)
        length = max(nums) + k - normal_scalar + 1
        line_sweep = [[0, 0] for _ in range(length)] # (start, end)
        for start, end in intervals:
            line_sweep[start][START] += 1
            line_sweep[end][END] += 1

        res = 0
        cur_overlap = 0
        for start, end in line_sweep:
            cur_overlap += start
            if cur_overlap > res:
                res = cur_overlap
            cur_overlap -= end

        return res
