class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        
        d = defaultdict(int)
        l = 0
        for r in range(len(s)):
            letter = s[r]
            d[letter] += 1

            count = sum(d.values())
            while count - max(d.values()) > k:
                d[s[l]] -= 1
                count -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
