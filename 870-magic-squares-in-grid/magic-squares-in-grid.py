class Solution:
    def __init__(self):
        self.grid = None
    def isOutOfBounds(self, r, c):
        row, col = len(self.grid), len(self.grid[0])
        return r < 0 or r + 2 >= row or c < 0 or c + 2 >= col
    def isMagicSquare(self, r, c):
        # (r, c) might be in grid, but can't have magic square
        # with (r, c) as top-left corner
        if self.isOutOfBounds(r, c):
            return False
        
        # Check all numbers distinct
        seen = set()
        for rowIndex in range(3):
            for colIndex in range(3):
                val = self.grid[r + rowIndex][c + colIndex]
                if val in seen or not (1 <= val <= 9):
                    return False
                seen.add(self.grid[r + rowIndex][c + colIndex])
        
        # Since numbers are distinct from 1 to 9, if it's a magic
        # square, the sums of each row, column, and diagonal must be 15
        SUM = 15

        negDiagSum = sum(self.grid[r + i][c + i] for i in range(3))
        if negDiagSum != SUM:
            return False
    
        posDiagSum = sum(self.grid[r + (2 - i)][c + i] for i in range(3))
        if posDiagSum != SUM:
            return False

        for rowIndex in range(3):
            rowSum, colSum = 0, 0
            for colIndex in range(3):
                rowSum += self.grid[r + rowIndex][c + colIndex]
                colSum += self.grid[r + colIndex][c + rowIndex]

            if rowSum != SUM or colSum != SUM:
                return False

        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        self.grid = grid
        r, c = len(grid) - 2, len(grid[0]) - 2
        return sum(self.isMagicSquare(i, j) for i in range(r) for j in range(c))