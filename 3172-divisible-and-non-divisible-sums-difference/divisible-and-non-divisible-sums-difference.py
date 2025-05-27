class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # SOLUTION 1:
        # num1, num2 = 0, 0
        # for num in range(1, n + 1):
        #     if num % m == 0:
        #         num2 += num
        #     else:
        #         num1 += num
        # return num1 - num2

        # SOLUTION 2:
        res = 0
        for num in range(1, n + 1):
            if num % m == 0:
                res -= num
            else:
                res += num
        return res