class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # return self.my_solution_without_aid(intervals, queries)

        # This solution is after looking at the Neetcode 150 Hints:
        LEFT, RIGHT = 0, 1
        SIZE, INTERVAL = 0, 1
        res, min_heap, query_sol = [], [], {}
        intervals.sort()

        index = 0
        for query in sorted(queries):
            while index < len(intervals) and (interval := intervals[index])[LEFT] <= query:
                index += 1
                heapq.heappush(min_heap, (interval[RIGHT] - interval[LEFT] + 1, interval))

            while min_heap and min_heap[0][INTERVAL][RIGHT] < query:
                heapq.heappop(min_heap)
            
            query_sol[query] = min_heap[0][SIZE] if min_heap else -1

        return list(map(lambda query: query_sol[query], queries))
        
    
    def my_solution_without_aid(self, intervals, queries):
        LEFT, RIGHT = 0, 1
        SIZE, INTERVAL = 0, 1
        line_sweep = defaultdict(lambda: defaultdict(int))
        for l, r in intervals:
            line_sweep[l][(l, r)] += 1
            # line_sweep[r]
            line_sweep[r + 1][(l, r)] -= 1
        #print(f"{line_sweep=}")

        d, query_sol, res = {}, {}, []
        min_heap = []
        times = sorted(line_sweep.keys())
        time_index = 0
        time = times[time_index]
        # for interval, freq in line_sweep[time].items():
        #     d[interval] = d.get(interval, 0) + freq
        #     if d[interval] == 0:
        #         del d[interval]
        time = float("-inf")

        for query in sorted(queries):
            if query in query_sol:
                continue
            
            # while time_index + 1 < len(times) and query <= times[time_index + 1]:
            while times[time_index] <= query:
                time = times[time_index]
                for interval, freq in line_sweep[time].items():
                    if interval not in d:
                        d[interval] = 0
                        l, r = interval
                        heapq.heappush(min_heap, (r - l + 1, interval))
                    d[interval] += freq
                    if d[interval] == 0:
                        del d[interval]
    
                time_index += 1
                # print(f"{time=}, {d=}")
            
            # while time > query:
            #     # Need to backtrack a step
            #     for interval, freq in line_sweep[time].items():
            #         d[interval] = d.get(interval, 0) + freq
            #         if d[interval] == 0:
            #             del d[interval]
            #     time_index -= 1
            #     time = times[time_index]
            
            # assert time >= query
            #print(f"{time == query=}")
            # query_sol[query] = (min(map(lambda interval: interval[RIGHT] - interval[LEFT] + 1, d.keys()), default = -1))
            # query_sol[query] = min([self.getSize(interval) for interval in d.keys()], default = -1)
            while min_heap and min_heap[0][INTERVAL] not in d:
                heapq.heappop(min_heap)
            query_sol[query] = min_heap[0][SIZE] if min_heap else -1
            # print(f"query_sol[{query}]={query_sol[query]}")

        #print(f"{query_sol=}")
        # return list(map(lambda query: query_sol[query], queries))
        return [query_sol[query] for query in queries]



        # LEFT, RIGHT = 0, 1
        # N = len(intervals)
        # intervals.sort(key = lambda interval: interval[RIGHT] - interval[LEFT] + 1)
        # sorted_queries = sorted(queries)

        # res = []
        # for query in queries:
        #     found_sol = False
        #     for left, right in intervals:
        #         if left <= query <= right:
        #             res.append(right - left + 1)
        #             found_sol = True
        #             break
            
        #     if not found_sol:
        #         res.append(-1)
        
        # return res

        # #print(f"{intervals=}")
        # for query in queries:
        #     # Find leftmost index leftmost in intervals such that intervals[leftmost][LEFT] <= query
        #     leftmost = None
        #     l, r = 0, N - 1
        #     while l <= r:
        #         mid = (l + r) // 2
        #         if intervals[mid][LEFT] <= query:
        #             # Valid solution, look for even leftmost ones!
        #             leftmost = mid
        #             r = mid - 1
        #         else:
        #             # Invalid solution, look for potentially valid ones on the right
        #             l = mid + 1
        #     # If no sol, return -1
        #     if leftmost is None:
        #         return -1

        #     # Find rightmost index r in intervals such that query <= intervals[r][RIGHT]
        #     rightmost = None
        #     l, r = 0, N - 1
        #     while l <= r:
        #         mid = (l + r) // 2
        #         if query <= intervals[mid][RIGHT]:
        #             # Valid solution, look for even rightmost ones!
        #             rightmost = mid
        #             l = mid + 1
        #         else:
        #             # Invalid solution, look for potentially valid ones on the left
        #             r = mid - 1
        #     # If no sol, return -1
        #     if rightmost is None:
        #         return -1

        #     #print(f"{query=}, {intervals[leftmost]=}, {intervals[rightmost]=}")


        # # intervals = [[1,4],[2,4],[3,6],[4,4]]
        # # queries = [2,3,4,5]

        # # line_sweep = [0,1,1,1,1,-3,0,-1]

        # # 

        # line_sweep = defaultdict(lambda: defaultdict(int))
        # for l, r in intervals:
        #     line_sweep[l][(l, r)] += 1
        #     line_sweep[r + 1][(l, r)] -= 1
        
        # #print(f"{line_sweep=}")

