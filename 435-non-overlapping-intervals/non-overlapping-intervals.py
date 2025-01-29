class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() # sort by increasing start time!

        prev_end = intervals[0][1]
        num_deletes = 0 # First interval guaranteed to overlap, hence start at one below 0!
        for i in range(1, len(intervals)):
            interval = intervals[i]
            start, end = interval

            # If no conflict, continue but UPDATE previous interval!
            if prev_end <= start:
                prev_end = end
                continue
            
            # I have to either delete the 'prev' interval or the
            # current interval. The idea is to be greedy in trying to
            # MINIMIZE the number of overall overlappings -- hence delete
            # the one with LARGER end time, as it can only be MORE likely
            # to overlap with the next interval's start time!
            # In other words, keep the one with SMALLER end time!
            num_deletes += 1
            if end < prev_end:
                prev_end = end

        return num_deletes
