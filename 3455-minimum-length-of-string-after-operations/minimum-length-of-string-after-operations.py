class Solution:
    def minimumLength(self, s: str) -> int:
        parities = defaultdict(lambda: 1)
        for letter in s:
            parities[letter] ^= 1
        # return len(d) + sum(freq % 2 == 0 for freq in freqs.values())
        # return sum(1 if freq % 2 else 2 for freq in freqs.values())
        # return len(freqs) + sum(freq % 2 == 0 for freq in freqs.values())
        return len(parities) + sum(parities.values())