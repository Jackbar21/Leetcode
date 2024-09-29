class AllOne:

    def __init__(self):
        self.d = {}
        self.min_heap = []
        self.max_heap = [] # w/ a min_heap, just use negative values instead!
        

    def inc(self, key: str) -> None:
        self.d[key] = self.d.get(key, 0) + 1
        # heapq.heappush(self.min_heap, (key, self.d[key]))
        # heapq.heappush(self.max_heap, (key, -self.d[key]))
        heapq.heappush(self.min_heap, (self.d[key], key))
        heapq.heappush(self.max_heap, (-self.d[key], key))
        

    def dec(self, key: str) -> None:
        assert key in self.d
        self.d[key] -= 1
        if self.d[key] == 0:
            del self.d[key]
            return
        
        # heapq.heappush(self.min_heap, (key, self.d[key]))
        # heapq.heappush(self.max_heap, (key, -self.d[key]))
        heapq.heappush(self.min_heap, (self.d[key], key))
        heapq.heappush(self.max_heap, (-self.d[key], key))
        
        

    def getMaxKey(self) -> str:
        ##print(self.d, self.max_heap)
        if len(self.d) == 0:
            return ""
        
        # key, val = ("", 0)
        # while self.d.get(key, -1) != val:
        #     key, val = heapq.heappop(self.max_heap)
        #     val = -val
        # val, key = self.max_heap[0]
        val, key = self.max_heap[0]
        # val = -val
        while key not in self.d or self.d[key] != -val:
            heapq.heappop(self.max_heap)
            val, key = self.max_heap[0]
        # val = -val

        # It's the largest, but should be back inside the heap!
        # heapq.heappush(self.max_heap, (key, -self.d[key]))
        return key
        return max(self.d, key=lambda k:self.d[k])

    def getMinKey(self) -> str:
        #print(self.d, self.max_heap, self.min_heap)
        if len(self.d) == 0:
            return ""
        
        # key, val = ("", 0)
        # while self.d.get(key, -1) != val:
        #     key, val = heapq.heappop(self.min_heap)
        # val, key = self.min_heap[0]
        val, key = self.min_heap[0]
        # val = -val
        while key not in self.d or self.d[key] != val:
            heapq.heappop(self.min_heap)
            val, key = self.min_heap[0]
        
        # It's the smallest, but should be back inside the heap!
        # heapq.heappush(self.min_heap, (key, self.d[key]))
        return key
        return min(self.d, key=lambda k:self.d[k])
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()