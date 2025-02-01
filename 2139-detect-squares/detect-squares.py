class DetectSquares:

    def __init__(self):
        self.d = {} # point-to-frequency mappings
        

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.d[point] = self.d.get(point, 0) + 1
        

    def count(self, point: List[int]) -> int:
        point_x, point_y = point
        res = 0
        # visited = set()
        # unvisited = set(self.d.keys())
        # unvisited.discard((point_x, point_y))
        # while len(unvisited) > 0:
        #     x, y = unvisited.pop()
        #     if abs(x - point_x) != abs(y - point_y):
        #         continue

        #     unvisited.discard((point_x, y))
        #     unvisited.discard((x, point_y))

        #     # Only add to res if it's a SQUARE and NOT a RECTANGLE!!!
        #     res += self.d[(x, y)] * self.d.get((point_x, y), 0) * self.d.get((x, point_y), 0)
        # return res

        for x, y in self.d:
            if (point_x, point_y) == (x, y):
                continue

            # Only add to res if it's a SQUARE and NOT a RECTANGLE!!!
            if abs(x - point_x) != abs(y - point_y):
                continue
            
            # if (x, y) in visited:
            #     continue
            # if (point_x, y) in visited:
            #     continue
            # if (x, point_y) in visited:
            #     continue
            
            # Treat point and other_point as corners of a square.
            # res = 1
            # res *= self.d[(x, y)]
            # res *= self.d.get((point_x, y), 0)
            # res *= self.d.get((x, point_y), 0)
            # if self.d.get((point_x, y), 0) > 0 and self.d.get((x, point_y), 0) > 0:
            #     res += self.d[(x, y)]
            res += self.d[(x, y)] * self.d.get((point_x, y), 0) * self.d.get((x, point_y), 0)
            # visited.add((x, y))
            # visited.add((point_x, y))
            # visited.add((x, point_y))

        return res


        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)