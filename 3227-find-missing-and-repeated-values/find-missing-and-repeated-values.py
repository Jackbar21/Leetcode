class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        s = set()
        a, b = None, None
        for row in grid:
            for num in row:
                if num in s:
                    a = num
                s.add(num)
        for num in range(1, pow(N, 2) + 1):
            if num not in s:
                b = num
                break
        return a, b