class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # alphabet = "abcdefghijklmnopqrstuvwxyz"
        # all_letters = alphabet + alphabet.upper()

        dt = defaultdict(int)
        for letter in t:
            dt[letter] += 1

        isSubset = lambda freq_dict: all(freq_dict[letter] >= dt[letter] for letter in dt) # O(1)
        d = defaultdict(int)
        
        min_length = float("inf")
        best_index = -1

        l = 0
        for r, letter in enumerate(s):
            d[letter] += 1
            if d[letter] < dt[letter]:
                continue
            if not isSubset(d):
                continue
            
            while True:
                left_letter = s[l]
                s_freq, t_freq = d[left_letter], dt[left_letter]
                if s_freq < t_freq:
                    break

                # They're equal, and we're about to remove this letter!
                # Hence, update result if possible :)
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    best_index = l
                
                # Loop Invariant
                d[left_letter] -= 1
                l += 1

                if s_freq == t_freq:
                    break # Now no longer supserset!
                    

                
            
            # while isSubset(d):
            #     if r - l + 1 < min_length:
            #         min_length = r - l + 1
            #         best_index = l
                
            #     # Loop Invariant
            #     d[s[l]] -= 1
            #     l += 1

        # print(f"{min_length=}, {best_index=}, {d=}, {dt=}")
        # One last time, in case solution is at end of string!
        if isSubset(d) and r - l + 1 < min_length:
            min_length = r - l + 1
            best_index = l
            
        return s[best_index: best_index + min_length] if best_index != -1 else ""
