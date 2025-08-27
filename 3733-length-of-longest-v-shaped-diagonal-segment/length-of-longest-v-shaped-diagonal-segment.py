class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.map = {
            (1, 1): (1, -1),    # down-right --> down-left
            (1, -1): (-1, -1),  # down-left  --> up-left
            (-1, -1): (-1, 1),  # up-left    --> up-right
            (-1, 1): (1, 1),     # up-right   --> down-right
        }
        self.memo = {}
        M, N = len(grid), len(grid[0])
        self.inBounds = lambda i, j: 0 <= i < M and 0 <= j < N

        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] != 1:
                    continue
                
                for di, dj in self.map:
                    length = self.dp(i, j, di, dj, 2, False)
                    if res < length:
                        res = length
        return res

    # Total Subproblems: 
    #   - M * N * 2 * 2 * 2 * 2 == O(M * N)
    # Time per Subproblem: 
    #   -
    # Total Complexity
    def dp(self, i, j, di, dj, next_square, has_turned):
        inBounds = self.inBounds
        if not inBounds(i, j):
            return 0

        if (i, j, di, dj, next_square, has_turned) in self.memo:
            return self.memo[(i, j, di, dj, next_square, has_turned)]

        # Case 1: Continue in current direction
        case1 = 1
        if inBounds(i + di, j + dj) and self.grid[i + di][j + dj] == next_square:
            case1 = 1 + self.dp(i + di, j + dj, di, dj, 0 if next_square == 2 else 2, has_turned)

        # Case 2: Change direction
        case2 = 1
        if not has_turned:
            new_di, new_dj = self.map[(di, dj)]
            case2 = self.dp(i, j, new_di, new_dj, next_square, True)
        
        res = case1 if case1 > case2 else case2
        self.memo[(i, j, di, dj, next_square, has_turned)] = res
        return res
