class Solution:
    def countAndSay(self, n: int) -> str:
        assert n >= 1
        if n == 1:
            return "1"
        
        digits = self.countAndSay(n - 1)

        prev_digit = digits[0]
        streak = 0
        res = []
        for digit in digits:
            if digit == prev_digit:
                streak += 1
                continue
            
            res.append(f"{streak}{prev_digit}")
            prev_digit = digit
            streak = 1
        
        if streak > 0:
            res.append(f"{streak}{prev_digit}")
        
        return "".join(res)