class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return any(comb[0] != "0" and (num := int("".join(comb))) == 2 ** int(math.log(num, 2)) for comb in itertools.permutations([digit for digit in str(n)]))