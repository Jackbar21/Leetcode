class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # O(n + klogn) solution!
        min_heap = [
            (
                point[0] ** 2 + point[1] ** 2,
                point
            )
            for point in points
        ]
        heapq.heapify(min_heap) # O(n)
        return list(heapq.heappop(min_heap)[1] for _ in range(k))
