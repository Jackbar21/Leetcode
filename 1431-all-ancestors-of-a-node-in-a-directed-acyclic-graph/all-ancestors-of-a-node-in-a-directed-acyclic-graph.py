class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        d = {i: set() for i in range(n)}

        for u, v in edges:
            d[v].add(u)
        
        # get ALL children of reversed edge graph
        for u in d:
            stack = [u]
            seen = set()
            while stack:
                node = stack.pop()
                for other_node in d[node]:
                    if other_node not in seen:
                        seen.add(other_node)
                        stack.append(other_node)
            d[u] = seen
        
        return [sorted(d[i]) for i in range(n)]