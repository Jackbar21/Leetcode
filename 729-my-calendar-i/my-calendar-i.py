class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for (other_start, other_end) in self.calendar:
            # if not (
            #     other_start <= other_end <= start <= end or
            #     start <= end <= other_start <= other_end
            # ):
            if not (
                other_end <= start or
                end <= other_start
            ):
                return False

        self.calendar.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

# start1 <= start2 <= end1

# s,e,start,end
# start,end,s,e
# s,start,e,end
# start,s,e,end