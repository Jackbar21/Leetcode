class Solution:
    def minWindow(self, s: str, t: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        all_letters = alphabet + alphabet.upper()

        dt = {letter: 0 for letter in all_letters}
        for letter in t:
            dt[letter] += 1

        isSubset = lambda freq_dict: all(freq_dict[letter] >= dt[letter] for letter in dt) # O(1)
        d = {letter: 0 for letter in all_letters}
        
        min_length = float("inf")
        best_index = -1

        l = 0
        for r, letter in enumerate(s):
            d[letter] += 1
            if d[letter] < dt[letter]:
                continue
            while isSubset(d):
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    best_index = l
                
                # Loop Invariant
                d[s[l]] -= 1
                l += 1

        # One last time, in case solution is at end of string!
        if isSubset(d) and r - l + 1 < min_length:
            min_length = r - l + 1
            best_index = l
            
        return s[best_index: best_index + min_length] if best_index != -1 else ""
