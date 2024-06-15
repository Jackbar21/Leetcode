class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x + 1):
            if i * i >= x:
                return i if i * i == x else i - 1