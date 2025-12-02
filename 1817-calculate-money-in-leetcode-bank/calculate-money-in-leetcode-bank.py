class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        sum_to_add = 1 + 2 + 3 + 4 + 5 + 6 + 7
        offs = 0
        while n > 7:
            n -= 7
            res += sum_to_add
            sum_to_add += 7
            offs += 1
        for i in range(1, n + 1):
            res += i + offs
        return res
