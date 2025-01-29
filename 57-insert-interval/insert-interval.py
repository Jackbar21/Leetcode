class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        START, END = 0, 1
        res = []
        for i, interval in enumerate(intervals):
            start, end = interval

            # Cannot start coalesce yet!
            if end < newInterval[START]:
                res.append(interval)
                continue
            
            # No more need to coalesce!
            if start > newInterval[END]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            
            # assert newInterval[START] <= newInterval[END] <= start <= end
            newInterval = (
                min(newInterval[START], start),
                max(newInterval[END], end)
            )


        # If returning through here, must be because we haven't inserted newInterval yet...
        # which can only be the case because it has the LARGEST start time!
        assert len(res) == 0 or newInterval[START] >= res[-1][END]
        res.append(newInterval)
        return res



