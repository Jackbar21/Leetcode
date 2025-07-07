class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        choices = [] # min_heap [(end, start)]
        line_sweep = defaultdict(list)

        for start, end in events:
            line_sweep[start].append((start, end))

        res = 0
        max_end = max(event[1] for event in events)
        for day in range(max_end + 1):
            for start, end in line_sweep[day]:
                heapq.heappush(choices, (end, start))
            found = False
            while choices:
                end, start = heapq.heappop(choices)
                if day <= end:
                    res += 1
                    break

        return res
