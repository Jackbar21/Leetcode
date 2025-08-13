class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # return n > 0 and n == 3 ** round(log(n, 3))

        if n <= 0:
            return False # 3^x > 0 for any integer x

        base = 1
        while base <= n:
            if base == n:
                return True
            base *= 3

        return False
