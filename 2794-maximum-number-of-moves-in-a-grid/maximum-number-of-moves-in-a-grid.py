class Solution:
    def __init__(self):
        self.grid = None
        self.memo = {}

        # Max row & col indices
        self.MAX_ROW = None
        self.MAX_COL = None

    def maxMoves(self, grid: List[List[int]]) -> int:
        self.grid = grid

        max_moves = 0
        for row_index in range(len(grid)):
            max_moves = max(max_moves, self.maxMovesFromPos(row_index, 0))
        
        # return max(0, max_moves - 1)
        return max_moves
    
    def inBounds(self, r, c):
        return 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0])
    
    def maxMovesFromPos(self, r, c):
        if (r, c) in self.memo:
            return self.memo[(r, c)]
        
        # Out of bounds
        # if not self.inBounds(r, c):
        #     return 0
        
        res = 0

        # Only consider VALID cases
        # for dr, dc in [(-1, 1), (0, 1), (1, 1)]:
        for dr in range(-1, 2):
            x, y = (r + dr), (c + 1)
            if self.inBounds(x, y) and self.grid[r][c] < self.grid[x][y]:
                case = 1 + self.maxMovesFromPos(x, y)
                res = max(res, case)
        
        self.memo[(r, c)] = res
        return res
        



