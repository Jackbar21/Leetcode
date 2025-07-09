class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        N = len(startTime)
        # assert N == len(startTime) == len(endTime)
        intervals = [(startTime[i], endTime[i]) for i in range(N)]
        # assert intervals == sorted(intervals)
        # print(f"{intervals=}")

        gaps = []
        prev_end = 0
        for start, end in intervals:
            diff = start - prev_end
            gaps.append(diff)
            prev_end = end
        gaps.append(eventTime - prev_end)

        cur_sum = 0
        for i in range(k + 1):
            cur_sum += gaps[i]

        res = cur_sum
        for i in range(k + 1, len(gaps)):
            cur_sum -= gaps[i - k - 1]
            cur_sum += gaps[i]
            if res < cur_sum:
                res = cur_sum
        return res


