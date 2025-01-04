class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ORD_A = ord("a")
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        border_indices = {letter: [None, None] for letter in alphabet}
        LEFTMOST, RIGHTMOST = 0, 1
        for i, letter in enumerate(s):
            if border_indices[letter][LEFTMOST] is None:
                border_indices[letter][LEFTMOST] = i
            else:
                border_indices[letter][RIGHTMOST] = i
        
        prefix_freq = []
        # freq_dict = {}
        freq_arr = [0] * 26
        for letter in s:
            # freq_dict[letter] = freq_dict.get(letter, 0) + 1
            # prefix_freq.append(freq_dict.copy()) # O(1) work, since at most 26 keys :)
            freq_arr[ord(letter) - ORD_A] += 1
            prefix_freq.append(freq_arr.copy())
        
        res = 0
        for letter in alphabet:
            if border_indices[letter][RIGHTMOST] is None:
                # Need at least 2 of the same letter to form any palindromes of length
                # 3 with it!!!
                continue
            
            l = border_indices[letter][LEFTMOST] + 1
            r = border_indices[letter][RIGHTMOST] - 1
            # di, dj = prefix_freq[l - 1], prefix_freq[r] # l > 0 always!!!
            # for key in dj:
            #     res += dj[key] > di.get(key, 0)
            ai, aj = prefix_freq[l - 1], prefix_freq[r]
            # res += sum(aj[idx] > ai[idx] for idx in range(26))
            for idx in range(26):
                res += aj[idx] > ai[idx]

        return res