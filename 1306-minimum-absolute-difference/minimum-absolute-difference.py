class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_key = float("inf")
        arr.sort()
        res = []
        prev = None
        for i, cur in enumerate(arr):
            if i == 0:
                prev = cur
                continue

            diff = cur - prev
            if diff > min_key:
                prev = cur
                continue
            
            if diff < min_key:
                min_key = diff
                res = []
            
            res.append((prev, cur))
            prev = cur
        
        return res