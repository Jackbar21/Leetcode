class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # sort by increasing start time!

        res = []
        overlap_start, overlap_end = intervals[0]
        for interval in intervals:
            start, end = interval
            if overlap_end < start:
                res.append((overlap_start, overlap_end))
                overlap_start, overlap_end = interval
                continue
            
            if start < overlap_start:
                overlap_start = start
            if end > overlap_end:
                overlap_end = end

        res.append((overlap_start, overlap_end))
        return res
