class Solution:
    def wordToDict(self, word):
        d = {}
        for letter in word:
            d[letter] = d.get(letter, 0) + 1
        return d
    def isAnagram(self, s: str, t: str) -> bool:
        return self.wordToDict(s) == self.wordToDict(t)