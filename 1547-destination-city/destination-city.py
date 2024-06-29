class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        for A, B in paths:
            if A not in d:
                d[A] = set()
            if B not in d:
                d[B] = set()
            d[A].add(B)
        
        print(d)
        for key in d:
            if len(d[key]) == 0:
                return key