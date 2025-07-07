class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # N = len(events)
        # events.sort()
        d = {}
        choices = [] # min_heap [(end, start)]
        min_start = float("inf")
        max_end = float("-inf")
        for start, end in events:
            if min_start > start:
                min_start = start
            if max_end < end:
                max_end = end
            
            if start not in d:
                d[start] = []
            d[start].append((start, end))

        res = 0
        index = 0
        for day in range(min_start, max_end + 1):
            # while index < N:
            #     start, end = events[index]
            #     if day < start:
            #         break
            #     heapq.heappush(choices, (end, start))
            #     index += 1
            for start, end in d.get(day, []):
                heapq.heappush(choices, (end, start))

            while choices:
                end, start = heapq.heappop(choices)
                if day <= end:
                    res += 1
                    break

        return res
