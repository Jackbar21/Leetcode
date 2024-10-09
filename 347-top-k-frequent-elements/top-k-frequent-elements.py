class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # BAD: O(nlogn)
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        # return sorted(set(nums), key=lambda num: d[num])[-k:]
        max_heap = []
        for num in d:
            heapq.heappush(max_heap, (-d[num], num))
        
        heapq.heapify(max_heap) # O(n)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res