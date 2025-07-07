class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        choices = [] # min_heap [(end, start)]
        line_sweep = defaultdict(list)

        for start, end in events:
            line_sweep[start].append((False, start, end))
            line_sweep[end + 1].append((True, start, end))
        
        res = 0
        for day in range(max(line_sweep.keys()) + 1):
            #print(f"{day=}")
            for is_over, start, end in line_sweep[day]:
                if not is_over:
                    heapq.heappush(choices, (end, start))
            #print(f"{choices=}")
            start = end = None
            while choices:
                end, start = heapq.heappop(choices)
                if day <= end:
                    break
                # else:
                    #print(f"{(start, end)} is INVALID. {banned=}")
                start = end = None
            #print(f"chosen=({start}, {end}), {choices=}")
            if start is not None and end is not None:
                #print(f"{day=}, {(start, end)=}")
                res += 1
            #print()

        return res
