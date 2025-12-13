class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        return list(map(lambda t: t[0], sorted([(c,b) for i,c in enumerate(code)if len(c)>0 and all(l.isalnum()or l=="_" for l in c) and(b:=businessLine[i]) in(k:=["electronics","grocery","pharmacy","restaurant"])and isActive[i]], key = lambda t: (k.index(t[1]),t[0]))))