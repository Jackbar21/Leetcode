class MyCalendarTwo:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        # start,end | s,e
        # start < e and end > s, then invalid
        conflicts = []
        for (s, e) in self.calendar:
            # if not (start < end <= s < e or s < e <= start < end):
            if start < e and end > s:
                # conflicts.append((s, e))
                for (cs, ce) in conflicts:
                    if cs < e and ce > s:
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