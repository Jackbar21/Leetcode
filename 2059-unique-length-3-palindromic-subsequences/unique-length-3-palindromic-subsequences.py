class Solution:
    def getSubarrayFrequencies(self, i, j):
        di, dj = self.prefix_freq[i - 1] if i > 0 else {}, self.prefix_freq[j]
        return {
            key: dj[key] - di.get(key, 0) # TODO: Consider not using defaultdict
            for key in dj
        }
    
    def getSubarrayFrequenciesCount(self, i, j):
        di, dj = self.prefix_freq[i - 1], self.prefix_freq[j]
        # return {
        #     key: dj[key] - di.get(key, 0) # TODO: Consider not using defaultdict
        #     for key in dj
        # }
        return sum(dj[key] > di.get(key, 0) for key in dj)

    def countPalindromicSubsequence(self, s: str) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        border_indices = {letter: [None, None] for letter in alphabet}
        LEFTMOST, RIGHTMOST = 0, 1
        for i, letter in enumerate(s):
            if border_indices[letter][LEFTMOST] is None:
                border_indices[letter][LEFTMOST] = i
            else:
                border_indices[letter][RIGHTMOST] = i
        
        prefix_freq = []
        freq_dict = {}
        for letter in s:
            freq_dict[letter] = freq_dict.get(letter, 0) + 1
            prefix_freq.append(freq_dict.copy()) # O(1) work, since at most 26 keys :)
        self.prefix_freq = prefix_freq

        res = 0
        for letter in alphabet:
            if border_indices[letter][RIGHTMOST] is None:
                # Need at least 2 of the same letter to form any palindromes of length
                # 3 with it!!!
                continue
            
            assert border_indices[letter][LEFTMOST] is not None
            l = border_indices[letter][LEFTMOST] + 1
            r = border_indices[letter][RIGHTMOST] - 1
            # d = self.getSubarrayFrequencies(l, r)
            # count = sum(val > 0 for val in d.values())
            di, dj = prefix_freq[l - 1], prefix_freq[r]
            # count = self.getSubarrayFrequenciesCount(l, r)
            count = sum(dj[key] > di.get(key, 0) for key in dj)
            res += count

        # print(f"{prefix_freq=}")
        # # print(f"{border_indices=}")
        return res