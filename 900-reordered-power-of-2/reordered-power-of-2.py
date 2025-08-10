class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return any(c[0]!="0"and(n:=int(''.join(c)))==2**int(log(n,2))for c in permutations(str(n)))