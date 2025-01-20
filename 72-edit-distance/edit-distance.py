class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.word1, self.word2 = word1, word2
        self.memo = {}
        return self.dp(0, 0)

    def dp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        if i >= len(self.word1) and j >= len(self.word2):
            return 0
        
        if j >= len(self.word2):
            # Can only delete characters from this point onwards!
            return len(self.word1) - i
        
        if i >= len(self.word1):
            # Can only insert characters from this point onwards!
            return len(self.word2) - j
        

        letter1, letter2 = self.word1[i], self.word2[j]

        # Case 1: Do nothing (letters already match!)
        case1 = float("inf")
        if letter1 == letter2:
            case1 = self.dp(i + 1, j + 1)
            self.memo[(i, j)] = case1
            return case1
        
        # Case 2: Insert a character
        case2 = 1 + self.dp(i, j + 1)

        # Case 3: Delete a character
        case3 = 1 + self.dp(i + 1, j)

        # Case 4: Replace a character
        case4 = 1 + self.dp(i + 1, j + 1)

        res = min(case1, case2, case3, case4)
        self.memo[(i, j)] = res
        return res
        
