class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                break
            i += 1
            j -= 1
        return i + 1 == j or (isPalindrome := lambda s: s == s[::-1])(s[i+1:j+1]) or isPalindrome(s[i:j])
