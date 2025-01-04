class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        border_indices = {letter: [None, None] for letter in alphabet}
        prefix_freq = [] # prefix_freq[i] = dict frequency count of each letter in s[0..i]
        freq_dict = {}
        LEFTMOST, RIGHTMOST = 0, 1
        for i, letter in enumerate(s):
            if border_indices[letter][LEFTMOST] is None:
                border_indices[letter][LEFTMOST] = i
            else:
                border_indices[letter][RIGHTMOST] = i
            
            freq_dict[letter] = freq_dict.get(letter, 0) + 1
            prefix_freq.append(freq_dict.copy()) # O(1) work, since at most 26 keys :)
        
        res = 0
        for letter in alphabet:
            if border_indices[letter][RIGHTMOST] is None:
                # Need at least 2 of the same letter to form any palindromes of length
                # 3 with it!!!
                continue
            
            l = border_indices[letter][LEFTMOST] + 1
            r = border_indices[letter][RIGHTMOST] - 1
            # dl, dr = prefix_freq[l - 1], prefix_freq[r] # l > 0 always!!!
            # for key in dr:
            #     res += dr[key] > dl.get(key, 0)
            hset = set()
            for index in range(l, r + 1):
                hset.add(s[index])
            res += len(hset)

        return res
