class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        digits = self.countAndSay(n - 1)
        prev_digit = digits[0]
        streak = 0
        res = []
        for digit in digits:
            if digit == prev_digit:
                streak += 1
            else:
                res.append(f"{streak}{prev_digit}")
                prev_digit = digit
                streak = 1

        # assert streak > 0
        res.append(f"{streak}{prev_digit}")

        return "".join(res)
       