class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        delta = 0
        deltas = []
        for diff in differences:
            delta += diff
            deltas.append(delta)
        # print(f"{deltas=}")

        # num + min_delta >= lower
        # <==> num >= lower - min_delta
        min_delta = min(deltas)

        # num + max_delta <= upper
        # <==> num <= upper - max_delta
        max_delta = max(deltas)

        lowest = max(lower, lower - min_delta)
        highest = min(upper, upper - max_delta)

        return highest - lowest + 1 if lowest <= highest else 0