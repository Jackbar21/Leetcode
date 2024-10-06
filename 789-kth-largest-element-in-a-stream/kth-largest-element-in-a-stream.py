class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(nums) # O(n)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

        # heap has n elements
        # and is a min_heap
        # and we heappop n - k times...
        # we are left with k elements, and necessarily, the LARGEST k elements

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)