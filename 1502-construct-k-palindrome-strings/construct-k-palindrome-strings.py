class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        d = defaultdict(int)
        for letter in s: d[letter] += 1
        return len(s) >= k and sum(map(lambda freq: freq % 2, d.values())) <= k
