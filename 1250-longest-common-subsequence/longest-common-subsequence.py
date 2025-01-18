class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        # self.text1, self.text2 = text1, text2
        # self.memo = {}
        # return self.dp(0, 0)

        # Let's try a bottom-up approach instead!
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                    continue
                
                case1, case2 = dp[i + 1][j], dp[i][j + 1]
                dp[i][j] = case1 if case1 > case2 else case2
    
        return dp[0][0]

    
    def dp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        # If we've "exhausted" one of the two strings,
        # then we have no more possible matchings :(
        if i >= len(self.text1) or j >= len(self.text2):
            return 0

        letter1, letter2 = self.text1[i], self.text2[j]

        # Case 1: letter1 == letter2, in which case you should ONLY consider this option!
        if letter1 == letter2:
            case1 = 1 + self.dp(i + 1, j + 1)
            self.memo[(i, j)] = case1
            return case1

        # Case 2: Shift index i by one (no matching!)
        case2 = self.dp(i + 1, j)

        # Case 3: Shift index j by one (no matching!)
        case3 = self.dp(i, j + 1)

        res = case2 if case2 > case3 else case3
        self.memo[(i, j)] = res
        return res
            