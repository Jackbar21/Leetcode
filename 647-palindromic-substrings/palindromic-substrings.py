class Solution:
    def countSubstrings(self, s: str) -> int:
        # 2D Dynamic Programming Solution!
        # self.s, self.memo = s, {}
        # res = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         res += self.dp2D(i, j)
        # return res

        # 1D Dynamic Programming Solution!
        res = 0 # Number of palindromic substrings!
        N = len(s)
        for center_index in range(N - 1):
            # Case 1: Odd length palindrome
            l, r = center_index, center_index
            res += 1
            while l >= 1 and r < N - 1 and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
                res += 1
            
            # Case 2: Even length palindrome
            l, r = center_index, center_index + 1
            if s[l] != s[r]:
                continue
            res += 1
            while l >= 1 and r < N - 1 and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
                res += 1
        
        # res + 1 to account for length-1 palindromic substring at s[-1]
        # that was not accounted for in the above for loop!
        return res + 1

    
    # dp2D(i, j) returns True if and only if s[i..j] is a palindrome! Otherwise, returns False
    def dp2D(self, i, j):
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
        
        res = self.dp2D(i + 1, j - 1)
        self.memo[(i, j)] = res
        return res