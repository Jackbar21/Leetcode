class Solution:
    def minimumLength(self, s: str) -> int:
        ORD_A = ord("a")
        d = [0] * 26
        for letter in s:
            d[ord(letter) - ORD_A] += 1
        return sum(1 if freq % 2 else 0 if freq == 0 else 2 for freq in d)