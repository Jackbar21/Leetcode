class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n: # TODO: maybe only do this if len(original) < m * n ?
            return []
        
        res = [
            [
                original[(n * j) + i] for i in range(n)
            ] 
            for j in range(m)
        ]
        return res
        
        res = [[]]
        for num in original:
            if len(res[-1]) < n:
                res[-1].append(num)
            else:
                res.append([num])
        
        return res