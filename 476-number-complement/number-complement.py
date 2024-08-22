class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join(str(1 - int(d)) for d in bin(num)[2:]), 2)
        