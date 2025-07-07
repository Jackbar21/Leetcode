class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        events.sort()

        choices = [] # min_heap [(end, start)]
        min_start = float("inf")
        max_end = float("-inf")
        for start, end in events:
            if min_start > start:
                min_start = start
            if max_end < end:
                max_end = end

        res = 0
        index = 0
        for day in range(min_start, max_end + 1):
            while index < N:
                start, end = events[index]
                if start != day:
                    break
                heapq.heappush(choices, (end, start))
                index += 1

            found = False
            while choices:
                end, start = heapq.heappop(choices)
                if day <= end:
                    res += 1
                    break

        return res
