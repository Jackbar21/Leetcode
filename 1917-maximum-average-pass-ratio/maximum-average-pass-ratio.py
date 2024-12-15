class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # (avg, pass_i, total_i)
        min_heap = [(-(((passing+1)/(total+1)) - (passing / total)), passing, total) for passing, total in classes] 
        heapq.heapify(min_heap)
        # print(f"{min_heap=}")

        for _ in range(extraStudents):
            _, passing, total = heapq.heappop(min_heap)
            # Add the extra brilliant student into the class!
            passing += 1
            total += 1
            new_ratio_increase = ((passing+1)/(total+1)) - (passing/total)
            heapq.heappush(min_heap, (-new_ratio_increase, passing, total))
            # print(f"{min_heap=}")
        
        # print(f"{min_heap}=")
        return sum(item[1]/item[2] for item in min_heap) / len(min_heap)
        