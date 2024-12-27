class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        cur_max = float("-inf")
        suffix_max = collections.deque([cur_max])
        for r in range(len(values) - 1, -1, -1):
            new_val = values[r] - r
            if new_val > cur_max:
                cur_max = new_val
            suffix_max.appendleft(cur_max)
        suffix_max.popleft()

        res = float("-inf")
        for i in range(len(values)):
            new_val = values[i] + i + suffix_max[i]
            if new_val > res:
                res = new_val
        return res
