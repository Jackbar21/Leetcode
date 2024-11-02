class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        
        d = defaultdict(int)
        l = 0
        for r in range(len(s)):
            letter = s[r]
            d[letter] += 1

            count = r - l + 1
            max_letter = max(d.values())
            while count - max_letter > k:
                d[s[l]] -= 1
                count -= 1
                l += 1
                # if s[l] == max_letter:
                #     max_letter = max(d.values())
            
            res = max(res, r - l + 1)
        
        return res
