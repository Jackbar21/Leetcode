class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        N = len(startTime)
        # assert N == len(startTime) == len(endTime)
        # intervals = [(startTime[i], endTime[i]) for i in range(N)]
        # assert intervals == sorted(intervals)

        # Firstly, we can move AT MOST one meeting, which means either 0 or 1!
        # So trivially, let's compute the current gaps for the 0 case :)
        gaps = []
        prev_end = 0
        for i in range(N):
            start, end = startTime[i], endTime[i]
            gap = start - prev_end
            gaps.append(gap)
            prev_end = end
        gaps.append(eventTime - prev_end)

        # 0 moved intervals case!
        res = max(gaps)

        # Interval at index i will have gaps[i] as left gap and gaps[i + 1] as right gap
        # Let's compute prefix and suffix maxes to help solve rest of problem later.
        cur_max = 0
        prefix_max = []
        for gap in gaps:
            if cur_max < gap:
                cur_max = gap
            prefix_max.append(cur_max)
        
        cur_max = 0
        suffix_max = []
        for gap in reversed(gaps):
            if cur_max < gap:
                cur_max = gap
            suffix_max.append(cur_max)
        suffix_max = suffix_max[::-1]

        # Now, loop through each interval. We know its right gap is gaps[i + 1], and
        # its left gap is gaps[i]. Let's say the interval itself is of size k. 
        # So if there exists any gap between gaps[0..i-1] or between gaps[i+2..] 
        # whose size is greater than or equal to k, we can fit the interval there and
        # realize gaps[i] + k + gaps[i + 1] as the maximal creatable size from this interval.
        # Otherwise, if no such large enough gap exists, we can move this interval as much
        # as left as possible to realize a total space of gaps[i] + gaps[i + 1] (i.e. not
        # including k).
        for i in range(N):
            start, end = startTime[i], endTime[i]
            interval_length = end - start

            left_gap, right_gap = gaps[i], gaps[i + 1]
            space = left_gap + right_gap

            left_max = prefix_max[i - 1] if i - 1 >= 0 else 0
            right_max = suffix_max[i + 2] if i + 2 < len(suffix_max) else 0
            max_usable_gap = left_max if left_max > right_max else right_max
            
            if interval_length <= max_usable_gap:
                space += interval_length
            if res < space:
                res = space

        return res
