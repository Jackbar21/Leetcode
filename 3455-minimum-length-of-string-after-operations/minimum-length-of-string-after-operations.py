class Solution:
    def minimumLength(self, s: str) -> int:
        freqs = defaultdict(int)
        for letter in s:
            freqs[letter] += 1
        return sum(1 if freq % 2 else 2 for freq in freqs.values())
