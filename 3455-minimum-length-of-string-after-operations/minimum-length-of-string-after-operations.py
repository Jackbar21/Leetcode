class Solution:
    def minimumLength(self, s: str) -> int:
        d = defaultdict(int)
        for letter in s:
            d[letter] += 1
        return sum(2 if freq % 2 == 0 else 1 for freq in d.values())