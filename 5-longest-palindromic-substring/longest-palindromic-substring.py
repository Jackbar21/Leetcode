class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.s, self.memo = s, {}
        longest, best_i, best_j = 0, 0, 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if j - i + 1 > longest and self.dp(i, j):
                    best_i, best_j = i, j
                    longest = j - i + 1
        return s[best_i: best_j + 1]

    def dp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        # Base Case: Odd length palindrome
        if i == j:
            return i == j
        
        # Base Case: Even length palindrome
        if i + 1 == j:
            return self.s[i] == self.s[j]

        # Base Case: Not a palindrome
        if i > j:
            return False
        
        if self.s[i] != self.s[j]:
            return False
        
        res = self.dp(i + 1, j - 1)
        self.memo[(i, j)] = res
        return res
