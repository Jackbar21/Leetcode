class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        line_sweep = defaultdict(int)
        for start, end in meetings:
            line_sweep[start] += 1
            line_sweep[end + 1] -= 1
        
        sorted_line_sweep = {key: line_sweep[key] for key in sorted(line_sweep.keys())}
        # sorted_days = sorted(line_sweep.keys())
        res = 0
        prev_day = 1
        active_intervals = 0
        # print(f"{line_sweep=}")
        print(f"{sorted_line_sweep=}")
        for key, val in sorted_line_sweep.items():
            day = key
            assert active_intervals >= 0
            if active_intervals == 0:
                res += day - prev_day
            prev_day = day
            # active_intervals += line_sweep[day]
            active_intervals += val
        
        # res += days - prev_day
        res += days - max(line_sweep.keys()) + 1
        return res