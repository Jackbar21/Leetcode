class Solution:
    def smallestNumber(self, n: int) -> int:
        # return int('1'*(len(bin(n))-2), 2)

        res = power = 0
        while n > 0:
            res += pow(2, power)
            power += 1
            n //= 2
        return res