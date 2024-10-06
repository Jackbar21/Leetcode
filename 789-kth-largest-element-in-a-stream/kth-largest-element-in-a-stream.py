class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(nums) # O(n)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # suppose have k (current largest) elements in stream
        # Case 1: val is part of NEW largest k
        #           there exists some element in heap such that val > element
        if len(self.heap) == self.k and val < self.heap[0]:
            return self.heap[0]
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)