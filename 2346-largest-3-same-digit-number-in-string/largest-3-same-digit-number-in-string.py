class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        max_digit = "0"
        for i in range(1, len(num) - 1):
            if num[i - 1] == (str_digit := num[i]) == num[i + 1]:
                if str_digit >= max_digit:
                    max_digit = str_digit
                    res = max_digit * 3
        return res
                