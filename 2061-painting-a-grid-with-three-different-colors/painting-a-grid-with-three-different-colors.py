class Solution:
    @cache
    def dp(self, col_index, prev_column):
        # Unlike the traditional Map-Coloring problem (requiring brute-force approach!),
        # We can leverage the fact that the grid is M x N in nature. We will keep track
        # of the current column index, as well as the colors of each position in the previous
        # column, which is at most M.
        M, N = self.M, self.N

        if col_index >= N:
            assert col_index == N
            return 1 # We found a valid solution!

        res = 0
        for permutation in self.permutations:
            # Valid if and only if each index has a different color from previous column!
            assert len(prev_column) == len(permutation) == M
            is_valid = all(prev_column[i] != permutation[i] for i in range(M))
            if is_valid:
                res += self.dp(col_index + 1, permutation)
        return res

    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = pow(10, 9) + 7
        RED, GREEN, BLUE, NO_COLOR = 0, 1, 2, 3
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        M, N = m, n
        self.M, self.N = M, N

        # Write a function to get every valid permutation of M colors in a column!
        permutations = []

        def backtrack(i):
            assert i > 0
            prev_color = arr[i - 1]

            if i == M:
                permutations.append(tuple(arr))
                return

            for color in [RED, GREEN, BLUE]:
                if color == prev_color:
                    continue
                
                arr.append(color)
                backtrack(i + 1)
                arr.pop()
        for color in [RED, GREEN, BLUE]:
            arr = [color] # to always have a prev_color!
            backtrack(1)
        
        assert len(permutations) == 3 * pow(2, M - 1)
        print(f"{len(permutations)=}")
        print(f"{permutations=}")
        self.permutations = permutations
        # return 1
        return self.dp(0, tuple([NO_COLOR] * M)) % MOD
        
            
            

        ### BACKTRACKING SOLUTION (START) ### -- Too slow!
        # Let's give backtracking a shot, even though there's nearly 100% chance this TLEs!
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
        return self.res % MOD
        ### BACKTRACKING SOLUTION (END) ### -- Too slow!

        # self.M, self.N = M, N
        # self.memo = {}
        # return self.dp(0, 0, {})
        # dp = [[NO_COLOR] * N for _ in range(M)]
        # for i in range(M):
        #     for j in range(N):
            





    
    
    # @cache
    # def dp(self, i, j, d):
    #     cache_key = (i, j, tuple(key, d[key] for key in sorted(d.keys())))
    #     if cache_key in self.memo:
    #         return self.memo[cache_key]

    #     RED, GREEN, BLUE, NO_COLOR = 0, 1, 2, 3
    #     M, N = self.M, self.N

    #     # Valid colors represents available options to us!
    #     valid_colors = set([RED, GREEN, BLUE])
    #     for color in [left, up, right, down]:
    #         valid_colors.discard(color)
        
    #     assert self.inBounds(i, j)
        
    #     # Termination case!
    #     if len(valid_colors) == 0:
    #         # We've hit a dead end (ran out of options), so no solution here!
    #         return 0

    #     if i == M - 1 and j == N - 1:
    #         # Got to the last cell, and len(valid_colors) > 0, so this is a plausible solution!
    #         return 1
        
    #     for color in valid_colors:
            
        

        
