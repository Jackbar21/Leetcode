class MyCalendarTwo:
    def __init__(self):
        self.calendar = [] # (start, end) sorted by increasing end times
   
    def book(self, start: int, end: int) -> bool:
        conflicts = []
        for (s, e) in self.calendar:
            if start < e and end > s:
                for (cs, ce) in conflicts:
                    if cs < e and ce > s:
                        return False

                conflicts.append((s, e))
        
        self.calendar.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)