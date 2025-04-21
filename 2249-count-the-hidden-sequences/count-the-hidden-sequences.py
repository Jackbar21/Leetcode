class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # For every num in 'hidden', it must be that lower <= num <= upper
        delta = 0
        deltas = []
        for diff in differences:
            delta += diff
            deltas.append(delta)

        # num + min_delta >= lower
        # <==> num >= lower - min_delta
        min_delta = min(deltas)
        if min_delta > 0:
            min_delta = 0

        # num + max_delta <= upper
        # <==> num <= upper - max_delta
        max_delta = max(deltas)
        if max_delta < 0:
            max_delta = 0

        lowest = lower - min_delta
        highest = upper - max_delta

        return highest - lowest + 1 if lowest <= highest else 0

# hidden = [h1, h2, h3, h4, ..., h_n, h_(n+1)]
# diffs  = [h2-h1, h3-h2, h4-h3, ..., h_(n+1)-h_n]