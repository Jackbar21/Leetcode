class MyCalendarTwo:
    def __init__(self):
        self.calendar = []

    def overlaps(self, s1, e1, s2, e2):
        # start, end = s1, e1
        # s, e = s2, e2
        # return start < e and end > s
        return s1 < e2 and e1 > s2
    def book(self, start: int, end: int) -> bool:
        # start,end | s,e
        # start < e and end > s, then invalid
        conflicts = []
        for (s, e) in self.calendar:
            # if not (start < end <= s < e or s < e <= start < end):
            if start < e and end > s:
                # conflicts.append((s, e))
                for (cs, ce) in conflicts:
                    if self.overlaps(cs, ce, s, e):
                        return False
                # interval = (start, e)
                # conflicts += 1
                # if conflicts >= 2:
                #     return False
                conflicts.append((s, e))
        
        self.calendar.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)