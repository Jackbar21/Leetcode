class Solution:
    def __init__(self):
        self.grid = None
        self.memo = {}

    def maxMoves(self, grid: List[List[int]]) -> int:
        self.grid = grid

        max_moves = 0
        for row_index in range(len(grid)):
            max_moves = max(max_moves, self.maxMovesFromPos(row_index, 0))
        
        return max_moves
    
    def inBounds(self, r, c):
        return 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0])
    
    def maxMovesFromPos(self, row, col):
        if (row, col) in self.memo:
            return self.memo[(row, col)]
        
        res = 0

        # Only consider VALID cases
        for x, y in [(row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]:
            if self.inBounds(x, y) and self.grid[row][col] < self.grid[x][y]:
                case = 1 + self.maxMovesFromPos(x, y)
                res = max(res, case)
        
        self.memo[(row, col)] = res
        return res
