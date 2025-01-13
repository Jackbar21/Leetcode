class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        self.memo = {}
        best_i, best_j = 0, 0
        longest = 1
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if self.dp(i, j) > longest:
                    longest = self.dp(i, j)
                    best_i = i
                    best_j = j
        return s[best_i:best_j+1]
        return max((self.dp(i, j) for i in range(len(s)) for j in range(i + 1, len(s))), default=1)
    
    def dp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        if i >= j:
            return i == j
        
        if self.s[i] != self.s[j]:
            # self.memo[(i, j)] = False
            return -1
        
        res = self.dp(i + 1, j - 1)
        res = res + 2 if res != -1 else -1
        self.memo[(i, j)] = res
        return res
        

