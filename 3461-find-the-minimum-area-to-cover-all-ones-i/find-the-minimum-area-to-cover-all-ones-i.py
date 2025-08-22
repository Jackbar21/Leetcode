class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # Answer will simply be first & last row that contains ANY number of ones.
        # Then for the columns, it'll similarly be first & last columns that contain ANY ones.
        M, N = len(grid), len(grid[0])
        rows_with_ones = set()
        cols_with_ones = set()

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    rows_with_ones.add(i)
                    cols_with_ones.add(j)
        
        min_row, max_row = min(rows_with_ones), max(rows_with_ones)
        min_col, max_col = min(cols_with_ones), max(cols_with_ones)
        return (max_row - min_row + 1) * (max_col - min_col + 1)
