class Solution:
    def minimumLength(self, s: str) -> int:
        d = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}
        for letter in s:
            d[letter] += 1
        return sum(0 if freq == 0 else 2 if freq % 2 == 0 else 1 for freq in d.values())