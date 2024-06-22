class Solution:
    def __init__(self):
        self.s = None # smaller string
        self.b = None # larger string
        self.memo = {}
    def isSubsequence(self, s, b):
        if len(s) <= 0:
            return True

        i = 0
        for letter in b:
            if letter == s[i]:
                i += 1
                if i >= len(s):
                    return True
        return False


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.s, self.b = (text1, text2) if len(text1) < len(text2) else (text2, text1)
        # want to find longest common subsequence of s inside b, since s is smaller
        # This will be true for some s[i:j], where 0 <= i <= j <= len(s)
        # We can use 2D Dynammic programming approach to solve this problem
        # We know that for all i, s[i:i] is the empty string and a valid subset
        # of length 0, meaning we could use that as our base for a bottom-up approach.
        # However, I usually tend to prefer top-down since it's more intuitive to me.
        # return self.longestComSub(0, len(s))
        return self.longestComSub(0, 0)
    def longestComSub(self, si, bi):
        if si >= len(self.s) or bi >= len(self.b):
            return 0
        
        if (si, bi) in self.memo:
            return self.memo[(si,bi)]
        
        if self.s[si] == self.b[bi]:
            self.memo[(si,bi)] = 1 + self.longestComSub(si+1,bi+1)
        else:
            self.memo[(si,bi)] = max(
                self.longestComSub(si+1,bi),
                self.longestComSub(si,bi+1)
            )
        
        return self.memo[(si,bi)]
        
