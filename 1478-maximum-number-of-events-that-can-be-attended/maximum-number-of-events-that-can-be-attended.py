class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        events.sort()

        choices = [] # min_heap [(end, start)]
        max_end = max(end for _, end in events)

        res = 0
        index = 0
        for day in range(events[0][0], max_end + 1):
            while index < N:
                start, end = events[index]
                if start != day:
                    break
                heapq.heappush(choices, (end, start))
                index += 1

            while choices:
                end, start = heapq.heappop(choices)
                if day <= end:
                    res += 1
                    break

        return res
