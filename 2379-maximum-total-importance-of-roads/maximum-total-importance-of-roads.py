class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d = {i: 0 for i in range(n)}

        for road in roads:
            ai, bi = road
            d[ai] += 1
            d[bi] += 1
        
        arr = sorted(d.keys(), key=lambda x:d[x], reverse=False)

        res = 0
        for i in range(len(arr)):
            res += d[arr[i]] * (i+1)
        return res