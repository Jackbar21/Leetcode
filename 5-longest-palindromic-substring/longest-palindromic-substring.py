class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 2D DP solution
        # self.s, self.memo = s, {}
        # longest, best_i, best_j = 0, 0, 0
        # for i in range(len(s)):
        #     for j in range(longest + i, len(s)):
        #         if self.dp2D(i, j):
        #             best_i, best_j = i, j
        #             longest = j - i + 1
        # return s[best_i: best_j + 1]
        # self.s, self.memo = s, {}
        
        # 1D "Fake" DP solution
        return self.dp1d(s)

    
    def dp1d(self, s):
        N = len(s)
        i, j = 0, 0
        longest = 1
        for center_index in range(N - 1):
            # Case 1: Odd length palindrome
            l, r = center_index, center_index
            while l >= 1 and r < N - 1 and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            if r - l + 1 > longest:
                i, j = l, r
                longest = r - l + 1
            
            # Case 2: Even length palindrome
            l, r = center_index, center_index + 1
            if s[l] != s[r]:
                continue
            while l >= 1 and r < N - 1 and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            if r - l + 1 > longest:
                i, j = l, r
                longest = r - l + 1
        
        return s[i: j + 1]

    def dp2D(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        # Base Case: Odd length palindrome
        if i == j:
            return True
        
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
