class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # For every num in 'hidden', it must be that lower <= num <= upper
        delta = 0
        min_delta, max_delta = 0, 0
        for diff in differences:
            delta += diff
            if delta < min_delta:
                min_delta = delta
            if delta > max_delta:
                max_delta = delta

        # num + min_delta >= lower
        # <==> num >= lower - min_delta
        lowest = lower - min_delta

        # num + max_delta <= upper
        # <==> num <= upper - max_delta
        highest = upper - max_delta

        return highest - lowest + 1 if lowest <= highest else 0
