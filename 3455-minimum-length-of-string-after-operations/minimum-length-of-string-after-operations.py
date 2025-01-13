class Solution:
    def minimumLength(self, s: str) -> int:
        # d = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}
        d = defaultdict(lambda: 1)
        for letter in s:
            d[letter] ^= 1 # Flip the bit!
        # return sum(0 if freq == 0 else 2 if freq % 2 == 0 else 1 for freq in d.values())
        return len(d) + sum(d.values())