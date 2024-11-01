class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        
        second_prev, prev = s[0], s[1]
        letters = [second_prev, prev]
        for i in range(2, len(s)):
            letter = s[i]
            if letter != second_prev or letter != prev:
                letters.append(letter)
            
            # Loop Invariant
            second_prev = prev
            prev = letter
        
        return ''.join(letters)