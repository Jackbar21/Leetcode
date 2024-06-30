class Solution:
    def __init__(self):
        self.haystack = None
        self.needle = None
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        self.haystack = haystack
        self.needle = needle
        return self.helper(0,0)
    def helper(self, i, j):
        if j >= len(self.needle):
            return i - j

        if i >= len(self.haystack):
            return -1        
        
        if self.haystack[i] == self.needle[j]:
            k = 1
            while (
                j+k < len(self.needle) 
                and i+k < len(self.haystack)
                and self.haystack[i+k] == self.needle[j+k]
            ):
                k += 1
            if k >= len(self.needle):
                return i
        
        return self.helper(i+1, 0)
            
