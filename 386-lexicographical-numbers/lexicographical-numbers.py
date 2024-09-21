class Solution:
    def __init__(self):
        self.n = None
        self.res = []
    def explore(self, num):
        if num > self.n:
            return
        self.res.append(num)
        num *= 10
        for _ in range(10):
            if num > self.n:
                return
            self.explore(num)
            num += 1
    def lexicalOrder(self, n: int) -> List[int]:
        self.n = n
        for starting_digit in range(1, 9 + 1):
            self.explore(starting_digit)
        return self.res