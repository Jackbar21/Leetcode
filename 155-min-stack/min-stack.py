class MinStack:

    def __init__(self):
        self.s = []
        self.min_s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.min_s) > 0 and self.min_s[-1] < val:
            val = self.min_s[-1]
        self.min_s.append(val)

    def pop(self) -> None:
        assert len(self.s) > 0 and len(self.min_s) > 0
        self.s.pop()
        self.min_s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        # return min(self.s)
        return self.min_s[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()