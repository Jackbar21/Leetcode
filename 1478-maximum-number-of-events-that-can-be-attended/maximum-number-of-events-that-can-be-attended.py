class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        choices = [] # min_heap [(end, start)]
        line_sweep = defaultdict(list)

        for start, end in events:
            line_sweep[start].append((False, start, end))
            # line_sweep[end + 1].append((True, start, end))
            line_sweep[end]
        
        res = 0
        for day in range(max(line_sweep.keys()) + 1):
            for is_over, start, end in line_sweep[day]:
                if not is_over:
                    heapq.heappush(choices, (end, start))
            found = False
            while choices:
                end, start = heapq.heappop(choices)
                if day <= end:
                    res += 1
                    break

        return res
