class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        d = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}
        for letter in s: d[letter] += 1
        return len(s) >= k and sum(map(lambda freq: freq % 2, d.values())) <= k
