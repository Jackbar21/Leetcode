class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        visited = set()
        attended = set()
        choices = [] # min_heap [(end, start)]
        line_sweep = defaultdict(list)

        for start, end in events:
            line_sweep[start].append((False, start, end))
            line_sweep[end + 1].append((True, start, end))
        # #print(f"{line_sweep=}")
        
        res = 0
        for day in range(max(line_sweep.keys()) + 1):
            #print(f"{day=}")
            for is_over, start, end in line_sweep[day]:
                if not is_over:
                    heapq.heappush(choices, (end, start))
                else:
                    visited.add((start, end))
            #print(f"{choices=}")
            start = end = None
            while choices:
                end, start = heapq.heappop(choices)
                if (start, end) not in visited and day <= end:
                    break
                # else:
                    #print(f"{(start, end)} is INVALID. {visited=}")
                start = end = None
            #print(f"chosen=({start}, {end}), {choices=}")
            if start is not None and end is not None:
                #print(f"{day=}, {(start, end)=}")
                res += 1
            #print()

        return res





        events.sort(key = lambda e: ((r := e[1]) - (l := e[0]), l, r))
        #print(f"{events=}")

        prev_end = float("-inf")
        res = 0
        for start, end in events:
            #print(f"{prev_end=}, {start=}, {end=}")
            # assert prev_end <= end
            # if not (prev_end <= end):
            #     continue
            # if prev_end > start:
            #     continue
            
            next_prev_end = max(prev_end + 1, start)
            if next_prev_end <= end:
                res += 1
                prev_end = next_prev_end
            #print(f"{next_prev_end=}, {res=}\n")
        return res
