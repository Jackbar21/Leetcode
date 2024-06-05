class Solution:
    def countSubstrings(self, s: str) -> int:
        # SUPROBLEMS TO SOLVE:
        """
        For each i,j, 1 <= i <= j <= len(s), let:
            L(i,j) = {
                1,      if s[i:j+1] is a palindrome
                0,      otherwise
            }
        """

        # SOLVING ORIGINAL PROBLEM:
        """
        The answer to our original problem is simply:
            sum(L(i,j) for i in range(len(s)) for j in range(len(s)))
        """

        # RECURSIVE FORMULA TO COMPUTE SUPROBLEMS:
        """
        L(i,j) = {
            1,              if i == j
            1,              if i < len(s), i+1==j, s[i]==s[j]
            1,              if 1 <= i+1 <= j-1 <= len(s),
                               L(i+1,j-1) == 1, s[i] == s[j]
            0,              otherwise      
        }
        """
        n = len(s)

        # Initialize L(i,j) to 0 for all i,j in range(1,n)
        L = [[0] * n for i in range(n)]

        # All strings of length k = 1 are palindromes
        for i in range(n):
            L[i][i] = 1
        
        # All strings of length k = 2 whose characters
        # are the same are palindromes
        for i in range(n-1):
            if s[i] == s[i+1]:
                L[i][i+1] = 1
        
        # Find all palindromic substrings of s[0:n] of length k>2
        for k in range(3,n+1):
            for i in range(n-k+1):
                j = i + k-1
                if ((L[i+1][j-1] == 1) and (s[i] == s[j])):
                    L[i][j] = 1
            
        num_palindromes = 0
        for i in range(n):
            for j in range(n):
                num_palindromes += L[i][j]
        
        return num_palindromes


