class Solution:
    def __init__(self):
        self.text1, self.text2 = None, None
        self.memo = {}
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.text1, self.text2 = text1, text2
        return self.lcs(0, 0)
    def lcs(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        self.memo[(i, j)] = (
            0 if i >= len(self.text1) or j >= len(self.text2)
            else 1 + self.lcs(i + 1, j + 1)
            if self.text1[i] == self.text2[j]
            else max(self.lcs(i + 1, j), self.lcs(i, j + 1))
        )

        return self.memo[(i, j)]
