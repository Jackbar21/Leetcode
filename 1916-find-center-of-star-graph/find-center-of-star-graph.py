class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        c1,c2 = edges[0]
        for i in range(1, len(edges)):
            edge = edges[i]
            if c1 not in edge:
                return c2
            if c2 not in edge:
                return c1