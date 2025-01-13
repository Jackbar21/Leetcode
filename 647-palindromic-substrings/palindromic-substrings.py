class Solution:
    def countSubstrings(self, s: str) -> int:
        self.s, self.memo = s, {}
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                res += self.dp(i, j)
        return res
    
    # dp(i, j) returns True if and only if s[i..j] is a palindrome! Otherwise, returns False
    def dp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        # Base Case 1: Even length palindrome
        if i + 1 == j:
            return self.s[i] == self.s[j]
        
        # Base Case 2: Odd length palindrome
        if i >= j:
            return i == j
        
        if self.s[i] != self.s[j]:
            return False
        
        res = self.dp(i + 1, j - 1)
        self.memo[(i, j)] = res
        return res