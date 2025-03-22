class MedianFinder:
    # TODO: REMEMBER TO DO THE FOLLOW UPS ONCE DONE WITH THE PROBLEM!!!
    def __init__(self):
        # Suppose there are currently N elements in TOTAL
        self.max_heap = [] # Max heap of N // 2 SMALLEST elements
        self.min_heap = [] # Min heap of N - len(self.max_heap) LARGEST elements

    def addNum(self, num: int) -> None:
        # if len(self.max_heap) == len(self.min_heap):
        #     heapq.heappush(self.min_heap, num)
        # else:
        #     heapq.heappush(self.max_heap, -num) # Simulate max heap via min heap w/ negative numbers
        if len(self.min_heap) == 0:
            self.min_heap.append(num)
            return
        
        if len(self.max_heap) == 0:
            # assert len(self.min_heap) == 1
            num1, num2 = num, self.min_heap.pop()
            small, big = (num1, num2) if num1 < num2 else (num2, num1)
            self.max_heap.append(-small)
            self.min_heap.append(big)
            return
        
        max_left = -self.max_heap[0]
        min_right = self.min_heap[0]
        if num < max_left:
            heapq.heappush(self.max_heap, -num)
        elif num > min_right:
            heapq.heappush(self.min_heap, num)
        else:
            # Push into whichever has smallest size, since we balance
            # heap right afterwards, we really could just pick randomly...
            if len(self.max_heap) < len(self.min_heap):
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
            # heapq.heappush(self.min_heap, num)


        # Balance heap stage
        # #print(f"PRE BALANCE: {self.max_heap=}, {self.min_heap=}")
        self.balance()
        # #print(f"POST BALANCE: {self.max_heap=}, {self.min_heap=}")
    
    def balance(self):
        MAX_LEN, MIN_LEN = len(self.max_heap), len(self.min_heap)
        if MAX_LEN == MIN_LEN:
            return
        if MAX_LEN == MIN_LEN - 1:
            return
        # if abs(MAX_LEN - MIN_LEN) <= 1:
        #     # Job finished!
        #     return
        
        # Max heap too large, add to min heap
        if MAX_LEN > MIN_LEN:
            max_num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, max_num)
            self.balance()
            return
        else:
            min_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_num)
            self.balance()
            return
        
    def findMedian(self) -> float:
        #print(f"FIND MEDIAN: {self.max_heap=}, {self.min_heap=}")
        N = len(self.max_heap) + len(self.min_heap)
        if N % 2 == 1:
            return self.min_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        
        # For any index i in a min heap, it's CHILDREN will be at indices 2*i+1 and 2*i+2.
        # Its PARENT will be at index i//2.
        # [1, 3, 3, 6, 7, 4, 6, 8]
        #            1
        #        /       \
        #      3           3
        #    /   \       /   \
        #   6     7     4     6
        #  /
        # 8

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
