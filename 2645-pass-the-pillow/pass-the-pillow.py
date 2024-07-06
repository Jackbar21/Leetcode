class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pos = time % (2*(n-1))
        if pos < n:
            return pos + 1
        
        pos -= n
        return n - pos - 1