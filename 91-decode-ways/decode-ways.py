class Solution:
    def __init__(self):
        self.length = 0
        self.memo = {}
    def numDecodings(self, s: str) -> int:
        self.length = len(s)
        # self.memo[len(s)] = 1
        return self.numDecPos(s, 0)
        
    def numDecPos(self, s, pos):
        if pos in self.memo:
            return self.memo[pos]
    
        if pos == self.length:
            return 1
        
        if s[pos] == "0":
            return 0
        
        
        self.memo[pos] = self.numDecPos(s, pos+1)
        if pos+1 < self.length and (
            s[pos] == "1" or 
            (s[pos] == "2" and 0 <= int(s[pos+1]) <= 6)
        ):
            self.memo[pos] += self.numDecPos(s, pos+2)
        
        return self.memo[pos]
        
