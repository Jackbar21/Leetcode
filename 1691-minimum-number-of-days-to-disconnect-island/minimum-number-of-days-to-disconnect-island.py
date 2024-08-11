class Solution:
    def __init__(self):
        self.grid = None
        self.visited = {} # (i, j)
    def minDays(self, grid: List[List[int]]) -> int:
        # Case 1: Less than one island
        # Case 2: Exactly one island (CONNECTED)
        # Case 3: More than one island
        self.grid = grid
        if self.numberOfIslands() != 1:
            # Graph already disconnected, so return 0
            return 0
        
        if len(self.visited) == 1:
            return 1
        
        if len(self.visited) == 2:
            return 2

        # A singular 1, is connected to AT MOST four 1s, and MINIMUM zero 0 1s
        # If zero 1s, then we have more than one island, so impossible
        # So every 1 in the island is connected to ONE - FOUR other ones.
        # Find the 1 with the MINIMUM number of connections to other ones.
        # So there will be at least one 1 that doesn't have a 1 to it's right.
        # Similar for top, down, and left.

        # If you take the RIGHTMOST 1 in the entire grid, and then find the
        # BOTTOMMOST 1 inside the COLUMN that the rightmost 1 is in, then
        # that 1 doesn't have a 1 to its right nor below it, meaning it can
        # only AT MOST have a 1 to the left of it and above it

        # This means, that there exists at least one 1 such that the MAXIMUM
        # number of 1s that it is connected to is 2. AND of course, since the
        # number of islands is EXACTLY one in this case, there must be at least
        # one 1 attached to this such one (with at most two attached ones) 
        # mentioned above.

        # This is the number of adjacent 1s to the 1 in the island with
        # the FEWEST number of 1s adjacent to it. Again, this number must
        # EITHER be EXACTLY 1, OR EXACTLY 2. No more, no less.
        min_val = min(self.visited.values())
        assert min_val == 1 or min_val == 2
        if min_val == 1:
            return 1
        
        rows = {i: 0 for i in range(len(grid))}
        cols = {i: 0 for i in range(len(grid[0]))}
        # pos_diags = {i: 0 for i in range(len(rows) + len(cols))} # row + col
        # neg_diags = {i: 0 for i in range(-len(cols), len(rows))} # row - col
        for pos in self.visited:
            row, col = pos
            if self.grid[row][col] == 1:
                rows[row] += 1
                cols[col] += 1
                # pos_diags[row + col] += 1
                # neg_diags[row - col] += 1
        
        if (min(rows.values()) == 1 
            or min(cols.values()) == 1
            # or min(pos_diags.values()) == 1
            # or min(neg_diags.values()) == 1
        ):
            return 1
        
        # Otherwise, loop through all the 1s in self.visited that
        # have exactly 2 adjacent ones, EXCEPT for the four "cornermost"
        # 1s, and then set its value in grid to 0, run numberOfIslands,
        # set back to 1 in grid, and return if numberOfIslands call != 1.

        # So first, find four "cornermost" 1s, to remove them from having
        # numberOfIslands (expensive call) called upon them
        ROW, COL = 0, 1
        _, rightmost_column = max(self.visited, key = lambda pos: pos[COL])
        _, leftmost_column =  min(self.visited, key = lambda pos: pos[COL])
        
        # Step 2: Find "deepest" 1 inside leftmost & rightmost columns
        left_topmost_row, right_topmost_row = float("inf"), float("inf")
        left_deepest_row, right_deepest_row = 0, 0
        for pos in self.visited:
            i, j = pos
            if j == rightmost_column:
                right_topmost_row = min(right_topmost_row, i)
                right_deepest_row = max(right_deepest_row, i)

            if j == leftmost_column:
                left_topmost_row = min(left_topmost_row, i)
                left_deepest_row = max(left_deepest_row, i)
        
        four_corners = [
            (left_topmost_row, leftmost_column),
            (left_deepest_row, leftmost_column),
            (right_topmost_row, rightmost_column),
            (right_deepest_row, rightmost_column),
        ]

        # Take all positions from self.visited that are NOT in four_corners
        # and whose number of adjacent ones is exactly 2.
        positions_to_check = list(filter(lambda pos: (
            self.visited[pos] <= 2 # should NOT be possible to be < 2
            and pos not in four_corners
        ), self.visited))
        print("FLAG MOMENT")
        print(self.visited)
        print("FLAG 2 MOMENT")
        print(positions_to_check)
        # return 2

        threes = list(filter(lambda pos: (
            self.visited[pos] == 3
            and pos not in four_corners
        ), self.visited))

        fours = list(filter(lambda pos: (
            self.visited[pos] >= 4 # should NOT be possible to be > 4
            and pos not in four_corners
        ), self.visited))

        prev_visited_set = {i: self.visited[i] for i in self.visited}
        # positions_to_check = [(2,3)]
        print("GOT HERE")
        for pos in positions_to_check + threes + fours:
            i, j = pos
            assert self.grid[i][j] == 1
            self.grid[i][j] = 0
            
            # 0 1 1
            # 1 1 1
            # 1 1 0

            self.visited.clear()
            if self.numberOfIslands() != 1:
                return 1
            self.visited = prev_visited_set
            assert len(prev_visited_set) == len(self.visited)
            for el in prev_visited_set:
                assert el in self.visited
                assert self.visited[el] == prev_visited_set[el]

            self.grid[i][j] = 1

        return 2

        



        return min(self.visited.values())

        # [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,0,1,1]]

        # 1 1 0 1 1
        # 1 1 1 1 1
        # 1 1 0 1 1
        # 1 1 1 1 1

        # 1 0
        # 0

        #                                     1
        #                           1 1 1 1 1 1
        #   1 1 1         1         1         1
        # 1 1 1 1 1 1 1 1 1 1 1 1 1 1         1
        #                                     1 --> no 1
        #                                     no one below
        #   1 1 1         1

        # Step 1: Find column of rightmost 1
        ROW, COL = 0, 1
        _, rightmost_column = max(self.visited, key = lambda pos: pos[COL])
        
        # Step 2: Find "deepest" 1 inside column from step 1
        deepest_row = 0
        for pos in self.visited:
            i, j = pos
            if j == rightmost_column:
                deepest_row = max(deepest_row, i)

        # This one has AT MOST two 1s next to it, 
        # and AT LEAST one 1 next to it
        # Case 1: only one neighbor 1
        # Case 2: two neighbor 1s

        left_pos = (deepest_row, rightmost_column - 1)
        above_pos = (deepest_row - 1, rightmost_column)



        if (not self.isInBounds(left_pos[ROW], left_pos[COL]) 
            or not self.isInBounds(above_pos[ROW], above_pos[COL])
        ):
            # There must be exactly one 1
            if self.isInBounds(left_pos[ROW], left_pos[COL]):
                i,j = left_pos
                assert not self.isInBounds(above_pos[ROW], above_pos[COL])
                assert self.grid[i][j] == 1
                return 1
            
            assert self.isInBounds(above_pos[ROW], above_pos[COL])
            i,j = above_pos
            assert self.grid[i][j] == 1
            return 1
        
        #      0
        #    0 1 -
        #      |
        assert self.isInBounds(left_pos[ROW], left_pos[COL]) and self.isInBounds(above_pos[ROW], above_pos[COL])
        if grid[left_pos[ROW]][left_pos[COL]] != 1:
            return 1
        if grid[above_pos[ROW]][above_pos[COL]] != 1:
            return 1
        
        # TODO: what if can disconnect island somewhere else with just 1 cut?
        return 2
        


        
    
    def numberOfIslands(self):
        number_of_islands = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 1 and (i,j) not in self.visited:
                    # self.visited.add((i,j))
                    self.visited[(i,j)] = self.getNumAdjacentOnes(i,j)
                    self.visitAllLandNeighbors(i, j)
                    number_of_islands += 1
        return number_of_islands

    def visitAllLandNeighbors(self, i, j):
        # up, down, left, right
        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        for direction in directions:
            di, dj = direction
            new_i, new_j = i + di, j + dj

            if (self.isInBounds(new_i, new_j) 
                and (new_i, new_j) not in self.visited
                and self.grid[new_i][new_j] == 1
            ):
                # self.visited.add((new_i, new_j))
                self.visited[(new_i, new_j)] = self.getNumAdjacentOnes(new_i, new_j)
                self.visitAllLandNeighbors(new_i, new_j)

    def getNumAdjacentOnes(self, i, j):
        # This is all O(1) work
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        num_ones = 0

        for direction in directions:
            di, dj = direction
            new_i, new_j = i + di, j + dj

            if (self.isInBounds(new_i, new_j)
                and self.grid[new_i][new_j] == 1
            ):
                # if (i,j) in [(3,2), (5,2)]:
                #     self.printGrid
                #     print(f"I,J --> {i},{j}")
                #     print(f"NEW_I,NEW_J --> {new_i},{new_j}")
                num_ones += 1
        # if (i,j) in [(3,2), (5,2)]:
        #     print(f"({i},{j}) --> {num_ones=}")
        return num_ones
    
    def isInBounds(self, i, j):
        return 0 <= i < len(self.grid) and 0 <= j < len(self.grid[i])
    
    def printGrid(self):
        for row in self.grid:
            print(" ".join(str(i) for i in row))