class AllOne:
    def __init__(self):
        self.d = {}
        self.min_heap = []
        self.max_heap = [] # w/ a min_heap, just use negative values instead!

    def inc(self, key: str) -> None:
        self.d[key] = self.d.get(key, 0) + 1
        heapq.heappush(self.min_heap, (self.d[key], key))
        heapq.heappush(self.max_heap, (-self.d[key], key))   

    def dec(self, key: str) -> None:
        # assert key in self.d
        self.d[key] -= 1
        if self.d[key] == 0:
            del self.d[key]
            return
        
        heapq.heappush(self.min_heap, (self.d[key], key))
        heapq.heappush(self.max_heap, (-self.d[key], key))

    def getMaxKey(self) -> str:
        if len(self.d) == 0:
            return ""
        
        val, key = self.max_heap[0]
        while self.d.get(key, 0) != -val:
            heapq.heappop(self.max_heap)
            val, key = self.max_heap[0]

        return key

    def getMinKey(self) -> str:
        if len(self.d) == 0:
            return ""
        
        val, key = self.min_heap[0]
        while self.d.get(key, 0) != val:
            heapq.heappop(self.min_heap)
            val, key = self.min_heap[0]

        return key

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()