class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        cur_max = float("-inf")
        suffix_max = []
        for j in range(len(values) - 1, 0, -1):
            new_val = values[j] - j
            if new_val > cur_max:
                cur_max = new_val
            suffix_max.append(cur_max)

        res = float("-inf")
        for i in range(len(values) - 1):
            new_val = values[i] + i + suffix_max[len(values) - 2 - i]
            if new_val > res:
                res = new_val
        return res
