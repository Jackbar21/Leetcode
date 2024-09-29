class Solution:
    def wordToDict(self, word):
        d = {}
        for letter in word:
            d[letter] = d.get(letter, 0) + 1
        return d
    def isAnagram(self, s: str, t: str) -> bool:
        # return self.wordToDict(s) == self.wordToDict(t)
        ds, dt = self.wordToDict(s), self.wordToDict(t)
        for letter in ds:
            if ds[letter] != dt.get(letter, 0):
                return False
        
        for letter in dt:
            if dt[letter] != ds.get(letter, 0):
                return False
        
        return True