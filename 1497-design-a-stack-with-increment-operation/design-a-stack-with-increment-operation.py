# Mr. Noor on YouTube inspired me to make my solution more efficient.
# My new idea is as follows:
"""
In the video I thought of a small optimization idea but quickly got turned away realizing that I'd have to keep track of intervals, but since we're always doing the k bottom elements, the interval is always [0, k]. I.e. the left index is always fixed (since it's always bottom k), so like you said we can keep track of these sizes to apply them again as an offset when popping.
"""
class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.d = {} # update via inc(), used by pop(). Now O(1) time.
        
    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        # Old solution:
        # print("pop", self.stack, self.d)
        # if len(self.stack) > 0:
        #     return self.stack.pop()
        # return -1

        if len(self.stack) == 0:
            return -1
        
        k = len(self.stack) - 1
        val = 0
        if k in self.d:
            val += self.d[k]
            self.d[k - 1] = self.d.get(k - 1, 0) + self.d[k]
            del self.d[k]
        return val + self.stack.pop()
        
    def increment(self, k: int, val: int) -> None:
        # Old Solution:
        # for i in range(min(k, len(self.stack))):
        #     self.stack[i] += val

        # Now O(1) time
        k = min(k, len(self.stack))
        self.d[k - 1] = self.d.get(k - 1, 0) + val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)