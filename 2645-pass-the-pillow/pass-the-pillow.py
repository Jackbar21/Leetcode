class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pos = time % (2*(n-1))
        return pos + 1 if pos < n else 2*n - pos - 1