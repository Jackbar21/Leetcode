class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return sorted(points, key=lambda x:x[0]**2+x[1]**2)[:k]
        min_heap = [(point[0]**2+point[1]**2, point) for point in points]
        heapq.heapify(min_heap)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res