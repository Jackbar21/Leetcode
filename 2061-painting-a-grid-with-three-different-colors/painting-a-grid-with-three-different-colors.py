class Solution:
    @cache
    def dp(self, col_index, prev_column):
        # Unlike the traditional Map-Coloring problem (requiring brute-force approach!),
        # We can leverage the fact that the grid is M x N in nature. We will keep track
        # of the current column index, as well as the colors of each position in the previous
        # column, which is at most M.
        M, N = self.M, self.N

        if col_index >= N:
            # assert col_index == N
            return 1 # We found a valid solution!

        res = 0
        for permutation in self.permutations:
            # Valid if and only if each index has a different color from previous column!
            # assert len(prev_column) == len(permutation) == M
            is_valid = True
            for i in range(M):
                if prev_column[i] == permutation[i]:
                    is_valid = False
                    break

            if is_valid:
                res += self.dp(col_index + 1, permutation)
                res %= self.MOD

        return res

    def colorTheGrid(self, m: int, n: int) -> int:
        self.MOD = pow(10, 9) + 7
        RED, GREEN, BLUE, NO_COLOR = 0, 1, 2, 3
        COLOR_OPTIONS = [RED, GREEN, BLUE]

        M, N = m, n
        self.M, self.N = M, N

        # Write a function to get every valid permutation of M colors in a column!
        permutations = []

        def backtrack(i):
            # assert i > 0
            if i == M:
                permutations.append(tuple(arr))
                return

            prev_color = arr[i - 1]
            for color in COLOR_OPTIONS:
                if color == prev_color:
                    continue
                arr.append(color)
                backtrack(i + 1)
                arr.pop()
        for color in [RED, GREEN, BLUE]:
            arr = [color] # to always have a prev_color!
            backtrack(1)
        
        # assert len(permutations) == 3 * pow(2, M - 1)
        self.permutations = permutations
        return self.dp(0, tuple([NO_COLOR] * M)) % self.MOD
        

        ### BACKTRACKING SOLUTION (START) ### -- Too slow!
        # Let's give backtracking a shot, even though there's nearly 100% chance this TLEs!
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        self.res = 0
        self.grid = [[NO_COLOR] * N for _ in range(M)]
        self.inBounds = lambda i, j: 0 <= i < M and 0 <= j < N
        def backtrack(i, j):
            grid, inBounds = self.grid, self.inBounds
            assert inBounds(i, j)
            valid_colors = set([RED, GREEN, BLUE])
            for di, dj in DIRECTIONS:
                neigh_i, neigh_j = i + di, j + dj
                if inBounds(neigh_i, neigh_j):
                    valid_colors.discard(grid[neigh_i][neigh_j])

            # Termination case!
            if len(valid_colors) == 0:
                # We've hit a dead end (ran out of options), so no solution here!
                # return 0
                return

            if i == M - 1 and j == N - 1:
                # Got to the last cell, and len(valid_colors) > 0, so this is a plausible solution!
                # return 1
                self.res += len(valid_colors)
                return
            
            next_i, next_j = (i + 1, 0) if j == N - 1 else (i, j + 1)
            assert inBounds(next_i, next_j)

            for color in valid_colors:
                assert grid[i][j] == NO_COLOR
                grid[i][j] = color

                backtrack(next_i, next_j)

                assert grid[i][j] == color
                grid[i][j] = NO_COLOR
            return
        
        backtrack(0, 0)
        return self.res % self.MOD
        ### BACKTRACKING SOLUTION (END) ### -- Too slow!
