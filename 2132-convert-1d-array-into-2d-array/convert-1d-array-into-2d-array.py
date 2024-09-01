class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n: # TODO: maybe only do this if len(original) < m * n ?
            return []
        
        res = [[]]
        # for num in original:
        for i in range(m * n):
            num = original[i]
            if len(res[-1]) < n:
                res[-1].append(num)
            else:
                res.append([num])
        
        return res
