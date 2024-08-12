class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            # Pop any elements that are not in the k-largest
            heapq.heappop(self.nums)


    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        # now, we have k + 1 elements
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)