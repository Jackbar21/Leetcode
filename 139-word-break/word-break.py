class Solution:
    def __init__(self):
        self.memo = {}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in self.memo:
            return self.memo[s]
        
        if len(s) <= 0:
            return True

        res = False
        for word in wordDict:
            if self.isSuffix(s, word):
                if self.wordBreak(s[:len(s)-len(word)], wordDict):
                    res = True
                    break
        
        self.memo[s] = res
        return res
        
    
    def isSuffix(self, word, suffix):
        if len(suffix) > len(word):
            return False
        
        offset = len(word) - len(suffix)

        for i in range(len(suffix)):
            if word[offset + i] != suffix[i]:
                return False
        
        return True


