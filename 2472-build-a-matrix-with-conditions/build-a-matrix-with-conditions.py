class Solution:
    # NOT MY OWN FUNCTION:
    def topsort(self, g, n):
        # -- Step 1 --
        indeg = [0] * n
        for u in g:
            for v in g[u]:
                indeg[v] += 1


        # -- Step 2 --
        q = []
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)

        # -- Step 3 and 4 --
        result = []
        while q:
            x = q.pop()
            result.append(x)
            for y in g[x]:
                indeg[y] -= 1
                if indeg[y] == 0:
                    q.append(y)

        return result

    def buildRow(self, k, conditions):
        d = defaultdict(list)
        for (parent, child) in conditions:
            d[parent-1].append(child-1)

        result = self.topsort(d, k)
        # Check if graph contains cycle
        if len(result) < k:
            return []

        return result

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        colConditions = list(set([(l,r) for (l,r) in colConditions]))
        rowConditions = list(set([(l,r) for (l,r) in rowConditions]))
        c = self.buildRow(k, colConditions)
        r = self.buildRow(k, rowConditions)

        if len(c) == 0 or len(r) == 0:
            return []
        
        matrix = [[0]*k for i in range(k)]
        c_lookup = {c[i]: i for i in range(len(c))}
        for i in range(k):
            # i represents us placing an element in i'th row (vertical)
            element_to_place = r[i]
            index = c_lookup.get(element_to_place, -1)
            assert index != -1
            matrix[i][index] = element_to_place + 1

        return matrix