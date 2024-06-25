class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                if d.get(s[i]) == t[i]:
                    continue
                return False

            d[s[i]] = t[i]
        
        return len(list(d.values())) == len(set(d.values()))
            

