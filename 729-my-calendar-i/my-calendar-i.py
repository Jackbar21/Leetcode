class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        s2, e2 = start, end
        for (s1, e1) in self.calendar:
            if not (
                s1 <= e1 <= s2 <= e2 or
                s2 <= e2 <= s1 <= e1
            ):
                return False

        self.calendar.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

# start1 <= start2 <= end1

# s1,e1,s2,e2
# s2,e2,s1,e1
# s1,s2,e1,e2
# s2,s1,e1,e2