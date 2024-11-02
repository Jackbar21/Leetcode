class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        res = 0

        l = 0
        for r in range(len(s)):
            letter = s[r]
            d[letter] = d.get(letter, 0) + 1
            while d[letter] > 1:
                d[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res