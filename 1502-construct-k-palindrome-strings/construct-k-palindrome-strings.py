class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        d = defaultdict(int)
        for letter in s:
            d[letter] += 1
        return len(s) >= k and sum(freq % 2 for freq in d.values()) <= k
