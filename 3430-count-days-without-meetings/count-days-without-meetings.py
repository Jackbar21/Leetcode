class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        line_sweep = defaultdict(int)
        for start, end in meetings:
            line_sweep[start] += 1
            line_sweep[end + 1] -= 1

        res = 0
        prev_day = 1
        active_intervals = 0
        sorted_days = sorted(line_sweep.keys())
        for day in sorted_days:
            # assert active_intervals >= 0
            if active_intervals == 0:
                res += day - prev_day

            # Loop Inavriant
            active_intervals += line_sweep[day] # Can be negative!
            prev_day = day
        
        # Last amount of days also matters
        res += days - day + 1
        return res
