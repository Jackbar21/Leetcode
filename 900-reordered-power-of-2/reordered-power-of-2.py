class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = []
        while n > 0:
            digits.append(str(n % 10))
            n //= 10

        for comb in itertools.permutations(digits):
            if comb[0] == "0":
                continue
            num = int("".join(comb))
            if num == 2 ** int(math.log(num, 2)):
                return True
        return False
