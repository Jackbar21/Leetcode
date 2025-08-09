class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n == 2 ** int(math.log(n, 2))
