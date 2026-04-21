class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True 

        # isPalindrome = lambda s: s == s[::-1]

        i, j = 0, len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                break
        
        if i + 1 == j:
            return True
        
        return isPalindrome(s[i+1:j+1]) or isPalindrome(s[i:j])
