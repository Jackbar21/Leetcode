class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        ORD_A, frequencies = ord("a"), [0] * 26
        for letter in s:
            frequencies[ord(letter) - ORD_A] += 1
        return len(s) >= k and sum(freq % 2 for freq in frequencies) <= k
