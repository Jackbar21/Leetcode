class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        ORD_A, frequencies = ord("a"), [0] * 26
        for letter in s:
            frequencies[ord(letter) - ORD_A] += 1
        
        odd_count = 0
        for freq in frequencies:
            odd_count += freq % 2
            if odd_count > k:
                return False
        return True
