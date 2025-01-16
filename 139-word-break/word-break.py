class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memo = {}
        self.word_dict = wordDict
        self.s = s
        return self.dp(0)
    
    # dp(i) == true if and only if can split s[i:]
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]
        
        if i >= len(self.s):
            return True

        string = self.s[i:]
        
        can_break = False
        for word in self.word_dict:
            if string.startswith(word) and self.dp(i + len(word)):
                can_break = True
                break
        
        self.memo[i] = can_break
        return can_break
