class Solution:
    def countAndSay(self, n: int) -> str:
        digits = [1]

        for _ in range(n - 1):
            prev_digit = digits[0]
            streak = 0
            res = []
            for digit in digits:
                if digit == prev_digit:
                    streak += 1
                else:
                    # res.append(f"{streak}{prev_digit}")
                    res.append(streak)
                    res.append(prev_digit)
                    prev_digit = digit
                    streak = 1

            if streak > 0:
                # res.append(f"{streak}{prev_digit}")
                res.append(streak)
                res.append(prev_digit)
            
            # digits = "".join(res)
            digits = res
        
        # return digits
        return "".join(str(digit) for digit in digits)