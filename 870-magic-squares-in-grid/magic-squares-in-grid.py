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
        
        neg_diag = [grid[r + i][c + i] for i in range(3)]
        # print(f"{neg_diag=}")
        SUM = sum(neg_diag)
    
        pos_diag = [grid[r + (2 - i)][c + i] for i in range(3)]
        # print(f"{SUM=}, {sum(pos_diag)=}")
        if sum(pos_diag) != SUM:
            return False
        for rowIndex in range(3):
            row = []
            col = []
            for colIndex in range(3):
                row.append(grid[r + rowIndex][c + colIndex])
                col.append(grid[r + colIndex][c + rowIndex])
            row_sum, col_sum = sum(row), sum(col)
            # print(f"{row_sum=}, {col_sum=}, {SUM=}")
            if sum(row) != SUM or sum(col) != SUM:
                return False

        assert SUM == 15
        return True



        

    def numMagicHelper(self, r, c):
        is_magic_square = self.isMagicSquare(r, c)

        
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        self.grid = grid
        # return self.numMagicHelper(0, 0)
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid)):
                count += int(self.isMagicSquare(r, c))
        return count
        # return 1 if self.isMagicSquare(0, 0) else 0

#  5 5
# 5 5 5
# 5 5 5