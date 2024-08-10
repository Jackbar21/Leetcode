class Solution:
    def __init__(self):
        self.visited = set()
        self.grid = None
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        dim = 3
        new_grid = [[0] * (dim * n) for _ in range(dim * n)]

        for i in range(n):
            for j in range(n):
                r, c = dim * i, dim * j
                if grid[i][j] == " ":
                    # " " -> 0 0 0
                    #        0 0 0
                    #        0 0 0
                    # Everything already 0, so do nothing!
                    pass
                elif grid[i][j] == "/":
                    # "/" -> 0 0 1
                    #        0 1 0
                    #        1 0 0
                    new_grid[r + 2][c] = 1
                    new_grid[r + 1][c + 1] = 1
                    new_grid[r][c + 2] = 1
                else:
                    if True:
                        # "\\" -> 1 0 0
                        #         0 1 0
                        #         0 0 1
                        new_grid[r][c] = 1
                        new_grid[r + 1][c + 1] = 1
                        new_grid[r + 2][c + 2] = 1
                    # first_backslash = not first_backslash
        
        # 1 1 1 1
        # 1 1 1 1
        # 1 1 1 1
        # 1 1 1 1

        print(new_grid)
        self.grid = new_grid
        number_of_regions = self.numberOfRegions()
        return number_of_regions
    
    def numberOfRegions(self):
        num_regions = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 0:
                    self.grid[i][j] = 1
                    self.visitAllZeroNeighbors(i, j)
                    num_regions += 1

        return num_regions
    
    def visitAllZeroNeighbors(self, i, j):
        # up, down, left, right
        for direction in [[-1,0], [1,0], [0, -1], [0, 1]]:
            di, dj = direction
            new_i, new_j = i + di, j + dj
            if (self.isInBounds(new_i, new_j)
                and self.grid[new_i][new_j] == 0):
                self.grid[new_i][new_j] = 1
                self.visitAllZeroNeighbors(new_i, new_j)
        return
    
    def isInBounds(self, i, j):
        return 0 <= i < len(self.grid) and 0 <= j < len(self.grid[i])

# / /
# / _

# 0 1 0 1
# 1 0 1 0
# 0 1 0 1
# 1 0 1 0

# 0 0 1     0 0 1
# 0 1 0     0 1 0
# 1 0 0     1 0 0
# 0 0 1     0 0 0
# 0 1 0     0 0 0
# 1 0 0     0 0 0

# 0 0 1 0 0 0
# 0 1 0 1 0 0
# 1 0 0 0 1 0
# 0 1 0 1 0 0
# 0 0 1 0 0 0
# 0 0 0 0 0 0