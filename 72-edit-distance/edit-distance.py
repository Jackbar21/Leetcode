class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.word1, self.word2 = word1, word2
        self.memo = {}
        return self.dp(0, 0)

    def dp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        # Base Case 1: We've "exhausted" every letter in word2.
        if j >= len(self.word2):
            # Can only delete characters from this point onwards!
            return len(self.word1) - i
        
        # Base Case 2: We've "exhausted" every letter in word1.
        if i >= len(self.word1):
            # Can only insert characters from this point onwards!
            return len(self.word2) - j

        # Base Case 3: If both letters already match, no need for any edits!
        if self.word1[i] == self.word2[j]:
            res = self.dp(i + 1, j + 1)
            self.memo[(i, j)] = res
            return res
        
        # Case 1: Insert a character
        case1 = 1 + self.dp(i, j + 1)

        # Case 2: Delete a character
        case2 = 1 + self.dp(i + 1, j)

        # Case 3: Replace a character
        case3 = 1 + self.dp(i + 1, j + 1)

        res = min(case1, case2, case3)
        self.memo[(i, j)] = res
        return res
