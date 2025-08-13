class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and n == 3**round(log(n, 3))