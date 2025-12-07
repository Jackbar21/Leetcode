class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.word1, self.word2 = word1, word2
        return self.dp(0, 0)
    
    @cache
    def dp(self, i, j):
        word1, word2 = self.word1, self.word2
        N, M = len(word1), len(word2)

        if i >= N:
            # We've used up all of word1, so only action left is to delete
            # all remaining letters from word2 (possibly zero)
            return M - j
        elif j >= M:
            # Similar to above, except we now delete remaining letters for word1
            return N - i
        
        letter_i, letter_j = word1[i], word2[j]

        # Case 1: Same letter, in which case we can skip
        case1 = float("inf") if letter_i != letter_j else self.dp(i + 1, j + 1)

        # Case 2: Insert a character in word1, specifically to match current letter from word2
        case2 = 1 + self.dp(i, j + 1)

        # Case 3: Insert a character in word2, specifically to match current letter from word1
        case3 = 1 + self.dp(i + 1, j)

        # Case 4: Replace current letter in word1 to one from word2 (or vise versa)
        case4 = 1 + self.dp(i + 1, j + 1)

        return min(case1, case2, case3, case4)