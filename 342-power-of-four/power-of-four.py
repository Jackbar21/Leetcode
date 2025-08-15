class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n == 4 ** round(math.log(n, 4))