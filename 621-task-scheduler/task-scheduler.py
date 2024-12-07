class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        for task in tasks:
            d[task] += 1
        
        min_heap = [(-d[task], task) for task in d]
        heapq.heapify(min_heap)

        # res = []
        res = 0
        while len(d) > 0:
            new_tasks = []
            for _ in range(n + 1):
                if len(min_heap) == 0:
                    res += 1
                    continue
                count, task = heapq.heappop(min_heap)
                count = -count
                # res.append(task)
                res += 1
                d[task] -= 1
                if d[task] == 0:
                    del d[task]
                    if len(d) == 0:
                        return res
                else:
                    new_tasks.append((1 - count, task)) # -(count - 1) == 1 - count :)
                    # heapq.heappush(min_heap, (1 - count, task))
            for item in new_tasks:
                heapq.heappush(min_heap, item)
        
        return res
