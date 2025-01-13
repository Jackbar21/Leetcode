class Solution:
    def minimumLength(self, s: str) -> int:
        d = defaultdict(lambda: 1)
        for letter in s:
            d[letter] ^= 1 # Flip the bit!
        return len(d) + sum(d.values())