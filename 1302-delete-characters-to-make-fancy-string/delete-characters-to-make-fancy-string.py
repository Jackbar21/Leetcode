class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        letters = [s[0], s[1]]
        for i in range(2, len(s)):
            if s[i] != s[i - 1] or s[i] != s[i - 2]:
                letters.append(s[i])
        
        return ''.join(letters)