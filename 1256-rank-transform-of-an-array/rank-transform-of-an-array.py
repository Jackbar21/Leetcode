class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) <= 0:
            return []

        sorted_arr = sorted(arr)
        d = {sorted_arr[0]: 1} 
        rank = 1
        for i in range(1, len(arr)):
            if sorted_arr[i] != sorted_arr[i - 1]:
                rank += 1
    
            num = sorted_arr[i]
            d[num] = min(d.get(num, rank), rank)

        return map(lambda num: d[num], arr)
