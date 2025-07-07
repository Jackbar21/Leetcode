class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        events.sort()

        choices = [] # min_heap [(end, start)]
        max_end = max(end for start, end in events)

        d = [[] for _ in range(max_end + 1)]
        for start, end in events:
            d[start].append((start, end))

        res = 0
        index = 0
        
        for day in range(max_end + 1):
            # while index < N:
            #     start, end = events[index]
            #     if start != day:
            #         break
            #     heapq.heappush(choices, (end, start))
            #     index += 1
            for start, end in d[day]:
                heapq.heappush(choices, (end, start))

            found = False
            while choices:
                end, start = heapq.heappop(choices)
                if day <= end:
                    res += 1
                    break

        return res
