class Solution:
    def smallestNumber(self, n: int) -> int:
        return int('1'*(len(bin(n))-2), 2)