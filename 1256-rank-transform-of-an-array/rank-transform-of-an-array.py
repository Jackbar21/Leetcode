class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) <= 0:
            return []

        d = {}
        rank = 1
        for num in sorted(set(arr)):
            # if num not in d:
            d[num] = rank
            rank += 1
                
        return map(lambda num: d[num], arr)

        # arr         == [37, 12, 28, 9, 100, 56, 80, 5, 12]
        # sorted(arr) == [5, 9, 12, 12, 28, 28, 28, 28, 28, 28, 37, 56, 80, 100]
        # d = {5: 1, 9: 2, 12: 3, 28: 4}
        # rank = 5
