class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        log = math.log(n,4)
        return log == int(log)