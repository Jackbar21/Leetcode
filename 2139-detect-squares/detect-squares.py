class DetectSquares:

    def __init__(self):
        self.d = {} # point-to-frequency mappings
        

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.d[point] = self.d.get(point, 0) + 1
        

    def count(self, point: List[int]) -> int:
        point_x, point_y = point
        res = 0

        for x, y in self.d:
            if (point_x, point_y) == (x, y):
                continue

            # Only add to res if it's a SQUARE and NOT a RECTANGLE!!!
            if abs(x - point_x) == abs(y - point_y):
                res += self.d[(x, y)] * self.d.get((point_x, y), 0) * self.d.get((x, point_y), 0)

        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)