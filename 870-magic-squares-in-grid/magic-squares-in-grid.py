class Solution:
    def __init__(self):
        self.grid = None
    def isOutOfBounds(self, r, c):
        grid = self.grid
        row = len(grid)
        col = len(grid[0])
        return r < 0 or r + 2 >= row or c < 0 or c + 2 >= col
    def isMagicSquare(self, r, c):
        grid = self.grid
        # (r, c) might be in grid, but can't have magic square
        # with (r, c) as top-left corner
        if self.isOutOfBounds(r, c):
            return False
        
        # Check all numbers distinct
        seen = set()
        for rowIndex in range(3):
            for colIndex in range(3):
                val = grid[r + rowIndex][c + colIndex]
                if val in seen or not (1 <= val <= 9):
                    return False
                seen.add(grid[r + rowIndex][c + colIndex])
        
        # Since numbers are distinct from 1 to 9, if it's a magic
        # square, the sums of each row, column, and diagonal must be 15
        SUM = 15

        negDiagSum = sum(grid[r + i][c + i] for i in range(3))
        if negDiagSum != SUM:
            return False
    
        posDiagSum = sum(grid[r + (2 - i)][c + i] for i in range(3))
        if posDiagSum != SUM:
            return False

        for rowIndex in range(3):
            rowSum, colSum = 0, 0
            for colIndex in range(3):
                rowSum += grid[r + rowIndex][c + colIndex]
                colSum += grid[r + colIndex][c + rowIndex]

            if rowSum != SUM or colSum != SUM:
                return False

        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        self.grid = grid
        r, c = len(grid), len(grid[0])
        return sum(self.isMagicSquare(i, j) for i in range(r) for j in range(c))