class Solution:
    def isPalindrome(self, word, l, r):
        if r - l + 1 <= 1:
            return True
        if l > r or l < 0 or r > len(word) or word[l] != word[r]:
            return False
        return self.isPalindrome(word, l+1, r-1)
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word, 0, len(word)-1):
                return word
        return ""