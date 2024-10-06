class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -abs(y - x))
        
        assert len(stones) <= 1
        return 0 if len(stones) == 0 else -stones[0]