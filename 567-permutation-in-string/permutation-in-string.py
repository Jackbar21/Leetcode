class Solution:
    def wordToDict(self, word):
        d = {}
        for letter in word:
            d[letter] = d.get(letter, 0) + 1
        return d
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if len(s1) == len(s2):
            return self.wordToDict(s1) == self.wordToDict(s2)
        
        d = self.wordToDict(s1)
        k = len(s1)
        for i in range(len(s2)-k+1):
            if self.wordToDict(s2[i:i+k]) == d:
                return True
        return False