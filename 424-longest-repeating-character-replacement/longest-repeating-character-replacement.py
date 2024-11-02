class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        l, res, max_letter = 0, 0, 0

        for r in range(len(s)):
            letter = s[r]
            d[letter] += 1
            max_letter = max(max_letter, d[letter])

            while r - l - max_letter >= k:
                d[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res
