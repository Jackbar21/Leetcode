class Solution:
    def minimumLength(self, s: str) -> int:
        d = defaultdict(int)
        for letter in s:
            d[letter] += 1
        return len(d) + sum(freq % 2 == 0 for freq in d.values())
        # return sum(1 if freq % 2 else 2 for freq in d.values())