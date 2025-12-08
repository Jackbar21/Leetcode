class Solution:
    def countTriples(self, n: int) -> int:
        return 2*((s:=set(b*b for b in range(n+1)))and sum(a*a+b*b in s for a in range(1,n+1) for b in range(a+1,n+1)))