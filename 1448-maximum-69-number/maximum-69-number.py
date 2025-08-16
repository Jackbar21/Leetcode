class Solution:
    def maximum69Number (self, num: int) -> int:
        changed = False
        res = []
        for digit in str(num):
            if not changed and digit == "6":
                res.append("9")
                changed = True
            else:
                res.append(digit)
        return int("".join(res))
