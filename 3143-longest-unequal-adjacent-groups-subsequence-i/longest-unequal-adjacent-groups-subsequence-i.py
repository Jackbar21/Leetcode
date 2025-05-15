class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        assert len(words) == len(groups)
        N = len(words)
        self.words, self.groups = words, groups
        self.memo = {}

        best_length = 0
        best_index = None
        for index in range(N):
            length = self.dp(index)
            print(f"self.dp({index})={self.dp(index)}")
            if length > best_length:
                best_length = length
                best_index = index
        assert best_index is not None
        
        # res = []
        # while best_index is not None:
        #     res.append(words[best_index])
        # return res[::-1]
        res = [words[best_index]]
        want_length = best_length - 1
        for index in range(best_index + 1, N):
            if self.dp(index) == want_length:
                res.append(words[index])
                want_length -= 1
                if want_length == 0:
                    break
        return res


    
    # Returns two item tuple:
    # (1) Length of longest alternating subsequence starting at index i
    # (2) Following index in longest alternating subsequence starting at index i
    def dp(self, i: int):
        if i in self.memo:
            return self.memo[i]
        
        N = len(self.words)
        if i >= N:
            return 0
        
        groups = self.groups
        group = groups[i]
        assert group in [0, 1]

        res = 1
        next_index = i
        for j in range(i + 1, N):
            if group != groups[j]:
                length = 1 + self.dp(j)
                if length > res:
                    res = length

        self.memo[i] = res
        return res
