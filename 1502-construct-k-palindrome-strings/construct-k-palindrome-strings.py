class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        d = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}
        for letter in s:
            d[letter] += 1
        return len(s) >= k and sum(val % 2 for val in d.values()) <= k
