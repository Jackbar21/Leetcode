class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        d = defaultdict(int)
        for letter in word:
            d[letter] += 1
        freqs = d.values()
        
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
                    max(0, freq - (base + k))
                )

                need_delete += case1 if case1 < case2 else case2
            
            if res > need_delete:
                res = need_delete
        
        return res
