class Solution:
    def minimumLength(self, s: str) -> int:
        d = defaultdict(int)
        for letter in s:
            d[letter] += 1
        return sum(2 if d[letter] % 2 == 0 else 1 for letter in d)