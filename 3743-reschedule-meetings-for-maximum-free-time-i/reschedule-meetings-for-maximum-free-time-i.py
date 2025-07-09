class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        N = len(startTime)
        assert N == len(startTime) == len(endTime)
        intervals = [(startTime[i], endTime[i]) for i in range(N)]
        assert intervals == sorted(intervals)
        print(f"{intervals=}")

        # l, r = 0, N - 1
        # prev_end = 0
        # next_start = eventTime
        # while k > 0 and (l < N or r >= 0):
        #     l_start, l_end = intervals[l] if l < N else (None, None)
        #     r_start, r_end = intervals[r] if r >= 0 else (None, None)
        #     if r_end == next_start:
        #         next_start = r_start
        #         r -= 1
        #         continue
        #     if l_start == prev_end:
        #         prev_end = l_end
        #         l += 1
        #         continue
            
        #     r_savings = next_start - r_end if r >= 0 else float("-inf")
        #     l_savings = l_start - prev_end if l < N else float("-inf")
        #     if r_savings > l_savings:
        #         print(f"r savings better, {intervals=}, {l, r=}")
        #         diff = r_end - r_start
        #         r_end = next_start
        #         r_start = r_end - diff
        #         print(f"UPDATED: {intervals[r]} TO: {r_start, r_end}")
        #         intervals[r] = (r_start, r_end)
        #         k -= 1
        #     else:
        #         print(f"l savings better, {intervals=}, {l, r=}")
        #         diff = l_end - l_start
        #         l_start = prev_end
        #         l_end = l_start + diff
        #         print(f"UPDATED: {intervals[l]} TO: {l_start, l_end}")
        #         intervals[l] = (l_start, l_end)
        #         k -= 1
        
        # print(f"OP: {intervals=}")




        # i = N - 1
        # next_start = eventTime
        # while k > 0 and i >= 0:
        #     start, end = intervals[i]
        #     if end == next_start:
        #         next_start = start
        #         i -= 1
        #         continue
            
        #     diff = end - start
        #     end = next_start
        #     start = end - diff
        #     print(f"UPDATED: {intervals[i]} TO: {start, end}")
        #     intervals[i] = (start, end)
        #     k -= 1
        
        # print(f"{intervals=}")

        # res = 0
        # next_start = eventTime
        # for start, end in reversed(intervals):
        #     diff = next_start - end
        #     print(f"{diff=}")
        #     next_start = start
        #     res = max(res, diff)
        # return max(res, start)

        gaps = []
        prev_end = 0
        for start, end in intervals:
            diff = start - prev_end
            gaps.append(diff)
            prev_end = end
        gaps.append(eventTime - prev_end)

        cur_sum = sum(gaps[:k + 1])
        res = cur_sum
        for i in range(k + 1, len(gaps)):
            cur_sum -= gaps[i - k - 1]
            cur_sum += gaps[i]
            res = max(res, cur_sum)
        return res


