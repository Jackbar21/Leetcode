class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        # Base Case: Empty list, or largest start interval
        if len(self.calendar) == 0 or self.calendar[-1][1] <= start:
            self.calendar.append((start, end))
            return True
        
        # Leftmost index in self.calendar such that start < self.calendar[index][1]
        index = self.leftmostBinarySearch(start, end)
        if end > self.calendar[index][0]:
            return False
        self.calendar.insert(index, (start, end))
        return True

    def leftmostBinarySearch(self, start, end):
        l, r = 0, len(self.calendar) - 1
        while l <= r:
            mid = (l + r) // 2
            if start < self.calendar[mid][1]:
                r = mid - 1
            else:
                l = mid + 1
        return l

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)