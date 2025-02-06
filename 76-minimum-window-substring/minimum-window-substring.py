class Solution: 
    def minWindow(self, s: str, t: str) -> str:
        # Idea: Unlike 'minWindowNaive', instead of using a dictionary for comparisons
        # (which yes is O(1) because s and t are only English letters, but otherwise WOULDN'T be!)
        # What we can do is grab the initially tightest window of s starting from the first index
        # that includes every letter in t (by starting with all of them, and shaving off the last one
        # as long as it doesn't become a subset!)
        # Then, we can keep restricting the window until we're no longer a subset of t, and remember which
        # letter we must FIND AGAIN to become a superset of t once more! This makes the algorithm O(m + n)!

        # Step 1: Make frequency dict of s and t
        ds, dt = defaultdict(int), defaultdict(int)
        for letter in s:
            ds[letter] += 1
        for letter in t:
            dt[letter] += 1

        # Step 2: Return "" if no such substring (since currently have ALL letters in s!)
        for letter in dt:
            if ds[letter] < dt[letter]:
                return ""
        
        # Step 2: Shave off last letter of s as long as still supserset of t!
        index = len(s) - 1
        letter = s[index]
        while ds[letter] > dt[letter]:
            ds[letter] -= 1
            index -= 1
            letter = s[index]
        
        # assert index >= 0
        min_length = index + 1
        best_index = 0

        # Remove last letter to make no longer subset of t
        ds[letter] -= 1
        needed_letter = letter
        
        l = 0
        for r in range(index, len(s)):
            letter = s[r]
            ds[letter] += 1
            if letter != needed_letter:
                continue
            
            # Found needed letter, so constrain the window size!
            needed_letter = None
            while needed_letter is None:
                left_letter = s[l]
                s_freq, t_freq = ds[left_letter], dt[left_letter]
                # assert s_freq >= t_freq

                if s_freq == t_freq:
                    needed_letter = left_letter
                    if r - l + 1 < min_length:
                        min_length = r - l + 1
                        best_index = l
                
                # Loop Invariant
                ds[left_letter] -= 1
                l += 1

        return s[best_index: best_index + min_length] if best_index != -1 else ""

    def minWindowNaive(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

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
            
            while l <= r:
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