class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base Case: Found a subsequence!
            if j >= len(t):
                return 1

            # Base Case: No letters left to use in s, and idn't find a subsequence!
            if i >= len(s):
                return 0

            s_letter, t_letter = s[i], t[j]

            # Case 1: If s_letter == t_letter, then have option of using it for new unique subsequence!
            case1 = dp(i + 1, j + 1) if s_letter == t_letter else 0

            # Case 2: Whether are not s_letter == t_letter, can simply skip s_letter!
            case2 = dp(i + 1, j)

            res = case1 + case2
            memo[(i, j)] = res
            return res

        return dp(0, 0)