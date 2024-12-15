class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # (increase in avg if you pick this value next, pass, total)
        min_heap = [((p/t) - ((p+1)/(t+1)), p, t) for p, t in classes]
        heapq.heapify(min_heap)

        for _ in range(extraStudents):
            _, passing, total = heapq.heappop(min_heap)
            # Add the extra brilliant student into the class!
            passing += 1
            total += 1
            new_ratio_increase = ((passing+1)/(total+1)) - (passing/total)
            heapq.heappush(min_heap, (-new_ratio_increase, passing, total))
        
        return sum(passing/total for _, passing, total in min_heap) / len(min_heap)
        
