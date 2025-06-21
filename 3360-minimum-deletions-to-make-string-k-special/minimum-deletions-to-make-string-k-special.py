class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freqs = [0] * 26
        ORD_A = ord("a")
        for letter in word:
            freqs[ord(letter) - ORD_A] += 1
        
        res = float("inf")
        for base in range(max(freqs) + 1):
            # Every number's freq must be in range [base, base + k]
            need_delete = 0
            for freq in freqs:
                # Only two cases for each letter (since we cannot add letters)

                # Case 1: Delete letter altogether
                case1 = freq

                # Case 2: Delete characters until inside range 
                case2 = (
                    float("inf") if freq < base else
                    0 if base <= freq <= base + k else
                    freq - (base + k)
                )

                need_delete += case1 if case1 < case2 else case2
            
            if res > need_delete:
                res = need_delete
        
        return res
