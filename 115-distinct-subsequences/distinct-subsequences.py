class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.s, self.t = s, t
        self.memo = {}
        res = self.dp(0, 0)
        print(f"{self.memo=}")
        return res
    
    def dp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        # Base Case: Found a subsequence!
        if j >= len(self.t):
            return 1

        # Base Case: No letters left to use in s, and idn't find a subsequence!
        if i >= len(self.s):
            return 0

        s_letter, t_letter = self.s[i], self.t[j]

        # Case 1: If s_letter == t_letter, then have option of using it for new unique subsequence!
        case1 = self.dp(i + 1, j + 1) if s_letter == t_letter else 0

        # Case 2: Whether are not s_letter == t_letter, can simply skip s_letter!
        case2 = self.dp(i + 1, j)

        res = case1 + case2
        self.memo[(i, j)] = res
        return res
