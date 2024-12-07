class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [
            (
                math.sqrt(pow(point[0], 2) + pow(point[1], 2)),
                point
            )
            for point in points
        ]
        heapq.heapify(min_heap)
        return [heapq.heappop(min_heap)[1] for _ in range(k)]