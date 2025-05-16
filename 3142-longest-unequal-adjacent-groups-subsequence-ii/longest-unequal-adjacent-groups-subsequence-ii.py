class Solution:
    @cache
    def isValidHammingDistance(self, i: int, j: int) -> bool:
        # Returns true if and only if hamming distance between words
        # at indices i and j is 1.
        words = self.words
        N = len(words)
        # assert 0 <= i < N
        # assert 0 <= j < N
        # assert i < j
        word_i, word_j = words[i], words[j]
        if len(word_i) != len(word_j):
            return False
        
        hamming_distance = 0
        for index, letter_i in enumerate(word_i):
            letter_j = word_j[index]
            if letter_i != letter_j:
                hamming_distance += 1
                if hamming_distance > 1:
                    return False
        return hamming_distance == 1

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        self.original_indices = {word: index for index, word in enumerate(words)}
        N = len(words)
        self.words, self.groups = words, groups
        self.memo = {}
        self.hamming_memo = {}

        best_length = self.dp(0)
        best_index = 0
        for index in range(1, N):
            length = self.dp(index)
            if best_length < length:
                best_length = length
                best_index = index
        
        res = [words[best_index]]
        want_length = best_length - 1
        for index in range(best_index + 1, N):
            if self.dp(index) == want_length:
                # Make sure it's valid!
                if groups[best_index] == groups[index]:
                    continue
                if not self.isValidHammingDistance(best_index, index):
                    continue

                res.append(words[index])
                want_length -= 1
                
                # Update best_index for next searching!
                best_index = index

                # if want_length == 0:
                #     break
        #print(f"{self.words=}")
        #print(f"{self.groups=}")
        sorted_memo = {i: self.memo[i] for i in sorted(self.memo.keys())}
        #print(f"self.memo={sorted_memo}")
        # return res
        res.sort(key = lambda word: self.original_indices[word])
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

        for j in range(i + 1, N):
            if group != groups[j] and self.isValidHammingDistance(i, j):
                res = max(res, 1 + self.dp(j))
        self.memo[i] = res
        return res
