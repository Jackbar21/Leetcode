class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_key = float("inf")
        arr.sort()
        res = []
        for i in range(1, len(arr)):
            prev, cur = arr[i - 1], arr[i]
            diff = cur - prev
            if diff > min_key:
                continue
            
            if diff < min_key:
                min_key = diff
                res = []
            
            res.append((prev, cur))
        
        return res