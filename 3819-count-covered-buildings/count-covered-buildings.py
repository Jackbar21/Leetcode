class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        min_x, max_x = defaultdict(lambda: float("inf")), defaultdict(lambda: float("-inf")) # min & max x values per y
        min_y, max_y = defaultdict(lambda: float("inf")), defaultdict(lambda: float("-inf")) # min & max y values per x
        for x, y in buildings:
            min_x[y] = min(min_x[y], x)
            max_x[y] = max(max_x[y], x)

            min_y[x] = min(min_y[x], y)
            max_y[x] = max(max_y[x], y)
        
        res = 0
        for x, y in buildings:
            if min_x[y] < x < max_x[y] and min_y[x] < y < max_y[x]:
                res += 1
        return res