class Solution:
    def __init__(self):
        self.s = None
    
    def minChanges(self, s: str) -> int:
        self.s = s
        # return self.minChangesDp(0, len(s) - 1)
        # return self.minChangesDp1D(1, s[0])
        res = 0

        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                res += 1
        
        return res
    
    # @cache
    def minChangesDp1D(self, i, prev_bit):
        if i >= len(self.s):
            return 0
        
        # Case 1: Flip the bit


        # Case 2: Don't flip the bit
    
    def minChangesDp(self, i, j, prev_bit = None):
        left_bit = self.s[i]
        while i < j and self.s[i] == left_bit:
            i += 1
        
        right_bit = self.s[j]
        while i < j and self.s[j] == right_bit:
            j -= 1
        
        if i >= j:
            assert i == j
            return 1 - int(self.s[i] == prev_bit)
        
        return 1 + min(
            self.minChangesDp(i + 1, j, self.s[i]),
            self.minChangesDp(i, j - 1, self.s[j])
        )