class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        # Skipping today
        return self.minimumSumEditorial(grid)

        # # Step 1: Find minimum
        # M, N = len(grid), len(grid[0])
        # rows_with_ones = set()
        # cols_with_ones = set()

        # for i in range(M):
        #     for j in range(N):
        #         if grid[i][j] == 1:
        #             rows_with_ones.add(i)
        #             cols_with_ones.add(j)
        
        # min_row, max_row = min(rows_with_ones), max(rows_with_ones)
        # min_col, max_col = min(cols_with_ones), max(cols_with_ones)
        # smallest_area = (max_row - min_row + 1) * (max_col - min_col + 1)
        # print(f"{min_row, max_row=}")
        # print(f"{min_col, max_col=}")
        # print(f"{smallest_area=}")
        
        # # Now, all that's left is to either increase by +1 the row or col index
        # # If we extend by a row index, we're adding + M.
        # # If we extend by a col index, we're adding + N.

        # # If #rows < #cols (i.e. M < N), then there's less area added if we extend
        # # a 
    
    def minimumSum2(
        self, grid: List[List[int]], u: int, d: int, l: int, r: int
    ) -> int:
        min_i = len(grid)
        max_i = 0
        min_j = len(grid[0])
        max_j = 0

        for i in range(u, d + 1):
            for j in range(l, r + 1):
                if grid[i][j] == 1:
                    min_i = min(min_i, i)
                    min_j = min(min_j, j)
                    max_i = max(max_i, i)
                    max_j = max(max_j, j)

        return (
            (max_i - min_i + 1) * (max_j - min_j + 1)
            if min_i <= max_i
            else sys.maxsize // 3
        )

    def rotate(self, vec: List[List[int]]) -> List[List[int]]:
        n = len(vec)
        m = len(vec[0]) if n > 0 else 0
        ret = [[0] * n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                ret[m - j - 1][i] = vec[i][j]

        return ret

    def solve(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        res = n * m

        for i in range(n - 1):
            for j in range(m - 1):
                res = min(
                    res,
                    self.minimumSum2(grid, 0, i, 0, m - 1)
                    + self.minimumSum2(grid, i + 1, n - 1, 0, j)
                    + self.minimumSum2(grid, i + 1, n - 1, j + 1, m - 1),
                )

                res = min(
                    res,
                    self.minimumSum2(grid, 0, i, 0, j)
                    + self.minimumSum2(grid, 0, i, j + 1, m - 1)
                    + self.minimumSum2(grid, i + 1, n - 1, 0, m - 1),
                )

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                res = min(
                    res,
                    self.minimumSum2(grid, 0, i, 0, m - 1)
                    + self.minimumSum2(grid, i + 1, j, 0, m - 1)
                    + self.minimumSum2(grid, j + 1, n - 1, 0, m - 1),
                )

        return res

    def minimumSumEditorial(self, grid: List[List[int]]) -> int:
        rgrid = self.rotate(grid)
        return min(self.solve(grid), self.solve(rgrid))