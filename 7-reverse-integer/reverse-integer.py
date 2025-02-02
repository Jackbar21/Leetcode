class Solution:
    def reverse(self, x: int) -> int:
        return (int(str(x)[::-1] if str(x)[0] != "-" else str(x)[1:][::-1]) * (-1 if str(x)[0] == "-" else 1)) if -pow(2, 31) <= (int(str(x)[::-1] if str(x)[0] != "-" else str(x)[1:][::-1]) * (-1 if str(x)[0] == "-" else 1)) <= pow(2, 31) - 1 else 0