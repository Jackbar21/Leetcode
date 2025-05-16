class Solution:
    def isValidHammingDistance(self, word1: str, word2: str) -> bool:
        # Returns true if and only if hamming distance between words
        # at indices i and j is 1.
        if len(word1) != len(word2):
            return False
        
        hamming_distance = 0
        for index, letter_i in enumerate(word1):
            letter_j = word2[index]
            if letter_i != letter_j:
                hamming_distance += 1
                if hamming_distance > 1:
                    return False
        return hamming_distance == 1

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        N = len(words)
        self.words, self.groups = words, groups
        self.memo = {}

        best_length = self.dp(0)
        best_index = 0
        for index in range(1, N):
            length = self.dp(index)
            if best_length < length:
                best_length = length
                best_index = index
        
        res = [words[best_index]]
        want_length = best_length - 1
        prev_index = best_index
        prev_word = words[prev_index]
        for index in range(prev_index + 1, N):
            if self.dp(index) == want_length:
                word = words[index]

                # Make sure it's valid!
                if groups[prev_index] == groups[index]:
                    continue
                if not self.isValidHammingDistance(prev_word, word):
                    continue

                res.append(word)
                want_length -= 1
                
                # Update best_index for next searching!
                prev_index = index
                prev_word = word

        return res

    def dp(self, i):
        if i in self.memo:
            return self.memo[i]

        words, groups = self.words, self.groups
        N = len(words)

        if i >= N:
            return 0
        
        # Return longest subsequence starting from index i
        res = 1
        group = groups[i]
        word = words[i]

        for j in range(i + 1, N):
            if group != groups[j] and self.isValidHammingDistance(word, words[j]):
                length = 1 + self.dp(j)
                if res < length:
                    res = length

        self.memo[i] = res
        return res
