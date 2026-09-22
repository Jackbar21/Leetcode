class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.M, self.N = len(self.grid), len(self.grid[0])
        self.inBounds = lambda x, y: 0 <= x < self.M and 0 <= y < self.N

    def adjacentSum(self, value: int) -> int:
        return self.directionsSum(value, [(0, 1), (1, 0), (-1, 0), (0, -1)])

    def diagonalSum(self, value: int) -> int:
        return self.directionsSum(value, [(1, 1), (1, -1), (-1, 1), (-1, -1)])

    def directionsSum(self, value: int, directions) -> int:
        res = 0
        for i in range(self.M):
            for j in range(self.N):
                for di, dj in directions:
                    if not self.inBounds(i + di, j + dj):
                        continue
                    if self.grid[i + di][j + dj] == value:
                        res += self.grid[i][j]
        return res
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)