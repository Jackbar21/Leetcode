class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        START, END = 0, 1
        intervals.sort(key = lambda interval: interval[START])

        res = []
        new_interval = intervals[0]
        for interval in intervals:
            start, end = interval
            if new_interval[END] < start:
                res.append(new_interval)
                new_interval = interval
                continue
            
            new_interval = (
                min(new_interval[START], start),
                max(new_interval[END], end)
            )



        # if new_interval is not None:
        #     res.append(new_interval)
        res.append(new_interval)
        return res