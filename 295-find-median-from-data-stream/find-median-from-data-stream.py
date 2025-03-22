# FOLLOW UPS:
    # - Q1: If all integer numbers from the stream are in the range [0, 100], 
    #       how would you optimize your solution?
    # 
    # - A1: addNum is O(log(n)), balance is O(1) [no need for recursive calls ever], findMedian is O(1)
    #       Hence I would look to somehow optimize addNum to probably be O(1). We can do this by simply
    #       keeping track of the FREQUENCIES of every single number in the range [0, 100] via a dictionary
    #       or even just an array. Adding a number would be as simple as increment that numbers frequency
    #       by 1 in that dictionary/array.
    #       As for findMedian, since we have a dictionary/array with at most 100-0+1 = 101 keys/indices,
    #       we can take the sum S of all the frequencies after O(101) == O(1) operations, use that as total
    #       number of elements, look for which number belongs to index S//2 (as well as S//2 - 1 if S is
    #       even) with again at most O(101) == O(1) operations. We leverage the fact that there are only
    #       a CONSTANT count of unique numbers to make both addNum and findMedian O(1) functions.
    #
    # - Q2: If 99% of all integer numbers from the stream are in the range [0, 100], 
    #       how would you optimize your solution?
    #       
    # - A2: In terms of asymptotic complexity, this technically might not be "better", but I would
    #       probably do something similar to the above. I would just additionally keep track of a
    #       dictionary/array for numbers LESS than 0 (their values and their frequencies), as well
    #       as for numbers GREATER than 0. addNum would still be an O(1) function of course, but
    #       SO WILL findNum! 
    #       The reason for this is that with above algorithm, if median were to be smaller than 0
    #       or greater than 100, then it might take O(.01*N) == O(N) time in worst case. However,
    #       by DEFINITION of MEDIAN, since 99% of the numbers are between [0, 100], the median
    #       number WILL BE in the range of numbers between [0, 100]! So we can simply keep track
    #       of just HOW MANY numbers are less than 0 and greater than 100, and simply include that
    #       in our solution for finding the median since we'll never encounter the problem of the median
    #       being less than 0 or greater than 100 (which would be what turns this into O(N) worst case.)
    #       Hence, findNum will still be O(1), and therefore be an improvement on the currently existing
    #       solution w/ heaps where addNum is O(log(N)) :)
class MedianFinder:
    def __init__(self):
        # Suppose there are currently N elements in TOTAL
        self.max_heap = [] # Max heap of (N // 2) SMALLEST elements
        self.min_heap = [] # Min heap of N - len(self.max_heap) LARGEST elements

    def addNum(self, num: int) -> None:
        MAX_LEN, MIN_LEN = len(self.max_heap), len(self.min_heap)
        if MIN_LEN == 0:
            # assert MAX_LEN == 0
            self.min_heap.append(num)
            return
        
        if MAX_LEN == 0:
            # assert MIN_LEN == 1
            num1, num2 = num, self.min_heap.pop()
            small, big = (num1, num2) if num1 < num2 else (num2, num1)
            self.max_heap.append(-small)
            self.min_heap.append(big)
            return
        
        # max(self.max_heap) <= max_left <= min_right <= min(self.min_heap)

        max_left = -self.max_heap[0]
        min_right = self.min_heap[0]
        if num < max_left:
            heapq.heappush(self.max_heap, -num)
        elif num > min_right:
            heapq.heappush(self.min_heap, num)
        else:
            # Push into whichever has smallest size, since we balance
            # heap right afterwards, we really could just pick randomly...
            if MAX_LEN < MIN_LEN:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)

        # Balance heap stage
        self.balance()
    
    def balance(self):
        MAX_LEN, MIN_LEN = len(self.max_heap), len(self.min_heap)
        # if (MAX_LEN == MIN_LEN) or (MAX_LEN == MIN_LEN - 1):
        #     return
        N = MAX_LEN + MIN_LEN
        if MAX_LEN == (N // 2):
            return

        # Max heap too large, add to min heap
        if MAX_LEN > MIN_LEN:
            max_num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, max_num)
        # Min heap too large, add to max heap
        else:
            min_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_num)
        
        # EDIT: Only once balance will ever be needed in total at a time,
        # making this function truly O(1) :)
        # Recursively balance further!
        # self.balance()
        
    def findMedian(self) -> float:
        MAX_LEN, MIN_LEN = len(self.max_heap), len(self.min_heap)
        N = MAX_LEN + MIN_LEN
        return self.min_heap[0] if (N % 2 == 1) else (-self.max_heap[0] + self.min_heap[0]) / 2
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
        # Hence, index 0 is always the MINIMUM of all values in the array (and where the heap tree starts!)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# N
# median is at index N//2 if array is odd (i.e. N%2==1)
# median is at indices (N//2 - 1) and N//2
# Element at index N//2 is LARGER THAN N//2 elements in TOTAL