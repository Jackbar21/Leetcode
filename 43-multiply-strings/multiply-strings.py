class Solution:
    def convertStringToNum(self, str_num):
        d = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        base = 10 ** (len(str_num) - 1)
        res = 0
        for digit in str_num:
            res += d[digit] * base
            base //= 10
        return res
    
    def convertNumToString(self, num):
        d = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        string_digits = []
        while True:
            string_digits.append(d[num % 10])
            num //= 10
            if num == 0:
                break
        return "".join(reversed(string_digits))

    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = self.convertStringToNum(num1), self.convertStringToNum(num2)
        return self.convertNumToString(num1 * num2)
