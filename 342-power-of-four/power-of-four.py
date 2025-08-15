class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # return n > 0 and n == 4 ** round(math.log(n, 4))

        base = 1
        while base < n:
            base *= 4
        return base == n