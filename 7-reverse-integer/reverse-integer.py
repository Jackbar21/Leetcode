class Solution:
    def reverse(self, x: int) -> int:
        digits = []
        sign = 1
        if x < 0:
            sign = -1
            x = -x

        while x != 0:
            digits.append(x % 10)
            x //= 10
        
        res = 0
        base = 1
        while len(digits) > 0:
            res += digits.pop() * base
            base *= 10

        res *= sign
        return res if -pow(2, 31) <= res <= pow(2, 31) - 1 else 0