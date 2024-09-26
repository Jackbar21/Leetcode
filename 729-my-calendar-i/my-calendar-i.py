class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
class MyCalendar:
    def __init__(self):
        self.calendar = []
        self.tree = None
    
    def insertNode(self, start, end):
        # DON'T WANT: s1 < e2 and s2 < e1
        # i.e....     s1 < e2 < e1 < s2 or s1 < e2 < s2 < e1
        if not self.tree:
            self.tree = TreeNode(start, end)
        
        


    def book(self, start: int, end: int) -> bool:
        for (other_start, other_end) in self.calendar:
            if other_end > start and end > other_start:
                return False

        self.calendar.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)