class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) <= 0:
            return []

        d = {}
        rank = 1
        for num in sorted(arr):
            if num not in d:
                d[num] = rank
                rank += 1
                
        return map(lambda num: d[num], arr)