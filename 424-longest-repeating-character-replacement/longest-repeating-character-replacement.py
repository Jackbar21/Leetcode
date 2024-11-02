class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        
        d = defaultdict(int)
        l = 0
        max_letter_val = 0
        max_letter = None
        for r in range(len(s)):
            letter = s[r]
            d[letter] += 1
            if d[letter] > max_letter_val:
                max_letter_val = d[letter]
                # max_letter = d[letter]

            # max_letter = max(d.values())
            while r - l - max_letter_val >= k:
                d[s[l]] -= 1
                l += 1
                # if s[l] == max_letter:
                #     max_letter = max(d.values())
                # if s[l] == max_letter:
                #     max_letter_val -= 1
            
            res = max(res, r - l + 1)
        
        return res
