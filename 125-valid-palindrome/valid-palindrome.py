class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c if c.isalnum() else '' for c in s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True       