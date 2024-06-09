class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        l = 0
        res = 0

        for i, letter in enumerate(s):
            while letter in hs:
                hs.remove(s[l])
                l += 1
            hs.add(letter)
            res = max(res, i - l + 1)
        
        return res