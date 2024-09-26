# class ListNode:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.next = None
class MyCalendar:
    def __init__(self):
        self.calendar = []
        # self.head = None

    def book(self, start: int, end: int) -> bool:
        # [SOL1]
        # self.insertNode(start, end)
        # [SOL2]
        # for (other_start, other_end) in self.calendar:
        #     if start < other_end and other_start < end:
        #         return False
        # return True
        # [SOL3]
        # i = 0
        # for (s, e) in self.calendar:
        #     if start < e:
        #         if s < end:
        #             return False
        #         else:
        #             self.calendar.insert(i, (start, end))
        #             return True
        #     i += 1
        START, END = 0, 1

        # List empty at start
        if len(self.calendar) == 0:
            self.calendar.append((start, end))
            return True

        # Add to start of array
        if end <= self.calendar[0][START]:
            self.calendar.insert(0, (start, end))
            return True
        
        # Add to end of array
        if self.calendar[-1][END] <= start:
            self.calendar.append((start, end))
            return True
        
        # Two elements case
        # if len(self.calendar) == 2:
            # Already handled add to start & end cases, so only consider adding to middle
        
        # If valid, element will be sandwhiched between two others!
        index = self.leftmostBinarySearch(start, end)
        if end > self.calendar[index][START]:
            return False
        self.calendar.insert(index, (start, end))
        return True
        return self.bookSearch(start, end, 0, len(self.calendar) - 1)

    def leftmostBinarySearch(self, start, end):
        START, END = 0, 1
        l, r = 0, len(self.calendar)
        leftmost = len(self.calendar) - 1

        while l <= r:
            mid = (l + r) // 2
            if start < self.calendar[mid][END]:
                leftmost = min(leftmost, mid)
                r = mid - 1
            else:
                l = mid + 1

        return leftmost
    def bookSearch(self, start, end, l, r):
        # if start >= e, look in right sub-half
        # if start < e, look in left subhalf
        # if e' comes before e, and e' < start < e, then have found right index
        # in which case return false if s < end, oterhwise append element
        # between e' and e representative intervals
        START, END = 0, 1

        if l >= r:
            if l > r:
                return False
            if start < self.calendar[l][END]:
                if self.calendar[l][START] < end:
                    return False
                self.calendar.insert(l, (start, end))
                return True
            elif start < self.calendar[l + 1][END]:
                if self.calendar[l + 1][START] < end:
                    return False
                self.calendar.insert(l + 1, (start, end))
                return True
            elif start < self.calendar[l - 1][END]:
                if self.calendar[l - 1][START] < end:
                    return False
                self.calendar.insert(l - 1, (start, end))
                return True
            else:
                assert False
            
        

        if l >= r:
            print("SPECIAL",l, r, start, end, self.calendar)
        else:
            print(l, r, start, end, self.calendar)

        mid = (l + r) // 2
        if self.calendar[mid - 1][END] < start < self.calendar[mid][END]:
            if self.calendar[mid][START] < end:
                return False
            else:
                self.calendar.insert(mid, (start, end))
                return True
        
        assert self.calendar[mid - 1][END] >= start or start >= self.calendar[mid][END]
        if self.calendar[mid - 1][END] >= start:
            # return self.bookSearch(start, end, mid, r)
            return self.bookSearch(start, end, l, mid - 1)
        else:
            assert start >= self.calendar[mid][END]
            return self.bookSearch(start, end, mid + 1, r)
        
    # def getInsertIndex(self, start, end):
    #     START, END = 0, 1
    #     l, r = 0, len(self.calendar)
    #     while l <= r:
    #         mid = (l + r) // 2
    #         if start < self.calendar[mid][END]:
    #             r = mid
    #         else:
    #             l = mid
    #     return l
    def insertNode(self, start, end):
        cur = self.head
        prev = None
        node = ListNode(start, end)
        if not self.head:
            self.head = ListNode(start, end)
            return True

        # sort by increasing finish times.
        # start, end
        # (s1,e1),(s2,e2),...,(s,e), (s',e') s.t. (start < e)
        # now if s < end, then this is not bookable
        # otherwise, insert the node here in place?
        while cur and start >= cur.end:
            # Loop Invariant
            prev = cur
            cur = cur.next
        
        # Reached end of list, so interval must be here! Might as well check it is valid
        if not cur:
            assert prev
            assert prev.end <= start
            prev.next = node
            return True
        
        # Not bookable
        if cur.start < end:
            return False
        
        # Bookable, so add right before cur
        if not prev:
            # Special Case: Add to very beginning of list
            node.next = self.head
            self.head = node
        else:
            prev.next = node
            node.next = cur
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)