class Solution:
    def reverse(self, x: int) -> int:
        digits = []
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        elif x == 0:
            return 0
        
        base = pow(10, math.ceil(math.log(x, 10)))
        res = 0
        while x != 0:
            base = base//10 if base > 10 else 1
            res += (x % 10) * base
            x //= 10
            

        res *= sign
        return res if -pow(2, 31) <= res <= pow(2, 31) - 1 else 0