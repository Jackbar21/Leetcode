class Solution:
    def convertStringToNum(self, str_num):
        d = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        base = 1
        res = 0
        for i in range(len(str_num) - 1, -1, -1):
            digit = str_num[i]
            res += d[digit] * base
            base *= 10
        return res

    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = self.convertStringToNum(num1), self.convertStringToNum(num2)
        return str(num1 * num2)

        
