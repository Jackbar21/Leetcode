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
        i = 0
        for (s, e) in self.calendar:
            if start < e:
                if s < end:
                    return False
                else:
                    self.calendar.insert(i, (start, end))
                    return True
            i += 1

        # List empty at start
        self.calendar.append((start, end))
        return True

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