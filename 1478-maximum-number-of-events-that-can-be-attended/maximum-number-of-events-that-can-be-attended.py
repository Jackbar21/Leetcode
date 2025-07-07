class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        min_start = float("inf")
        max_end = float("-inf")
        d = {}
        for start, end in events:
            if min_start > start:
                min_start = start
            if max_end < end:
                max_end = end
            
            if start not in d:
                d[start] = [end]
            else:
                d[start].append(end)

        choices = [] # min_heap [(end, start)]
        res = 0
        index = 0
        for day in range(min_start, max_end + 1):
            for end in d.get(day, []):
                heapq.heappush(choices, (end, day))

            while choices:
                end, start = heapq.heappop(choices)
                if day <= end:
                    res += 1
                    break

        return res
