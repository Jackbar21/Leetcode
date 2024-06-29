class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        possible = set()
        impossible = set()
        for A, B in paths:
            impossible.add(A)
            if A in possible:
                possible.remove(A)   
            if B not in impossible:
                possible.add(B)

        return list(possible)[0]