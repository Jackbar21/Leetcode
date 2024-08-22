class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join('0' if d == '1' else '1' for d in bin(num)[2:]), 2)