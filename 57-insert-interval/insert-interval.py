class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        res = []
        for i, interval in enumerate(intervals):
            start, end = interval

            # Cannot start coalesce yet!
            if end < new_start:
                res.append(interval)
                continue
            
            # No more need to coalesce!
            if start > new_end:
                res.append((new_start, new_end))
                res.extend(intervals[i:])
                return res
            
            # We must coalesce! Instead of adding anything to res, we will
            # simply update newInterval to reflect the coalescing of current
            # 'newInterval' with this current interval!
            if start < new_start:
                new_start = start
            if end > new_end:
                new_end = end

        # If returning through here, must be because we haven't inserted newInterval yet...
        # which can only be the case because it has the LARGEST start time!
        res.append((new_start, new_end))
        return res
