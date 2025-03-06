class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        s = set(range(1, pow(N, 2) + 1))
        a, b = None, None
        for row in grid:
            for num in row:
                if num not in s:
                    a = num
                else:
                    s.remove(num)
        b = s.pop()
        return a, b