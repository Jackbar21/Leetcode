class Solution:
    def isValidPosition(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n and (x, y) not in self.walls_set
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        guards.sort(), walls.sort()
        guards_set = set((row, col) for row, col in guards)
        walls_set = set((row, col) for row, col in walls)
        for i in range(len(guards)):
            guards[i] = tuple(guards[i])
        wall_rows = {i: [] for i in range(m)}
        wall_cols = {j: [] for j in range(n)}
        for row, col in walls:
            wall_rows[row].append(col)
            wall_cols[col].append(row)
        for key in wall_rows:
            wall_rows[key].sort()
        for key in wall_cols:
            wall_cols[key].sort()

        LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3
        guard_spots = {
            guard: [0, n - 1, 0, m - 1] for guard in guards # Left, Right, Up, Down
        }
        #print(wall_rows)
        #print(wall_cols)

        # For each guard, calculate the four positions (left, right, up, down) that it
        # is able to see up to. I.e. for each, the closest wall index in that direction,
        # or otherwise the very first out-of-bounds index in that direction to denote no
        # blocking walls in that direction.
        for guard in guards:
            guard_x, guard_y = guard
            # Find largest (rightmost) wall index smaller than (left of) guard_x
            wall_indices = wall_rows[guard_x]
            l, r = 0, len(wall_indices) - 1
            largest = -1
            while l <= r:
                mid = (l + r) // 2
                if wall_indices[mid] < guard_y:
                    largest = max(largest, wall_indices[mid])
                    l = mid + 1
                else:
                    r = mid - 1
            guard_spots[guard][LEFT] = largest

            # Find smallest (leftmost) wall index larger than (right of) guard_x
            wall_indices = wall_rows[guard_x]
            l, r = 0, len(wall_indices) - 1
            smallest = n
            while l <= r:
                mid = (l + r) // 2
                if wall_indices[mid] > guard_y:
                    smallest = min(smallest, wall_indices[mid])
                    # largest = max(largest, wall_rows[mid])
                    # l = mid + 1
                    r = mid - 1
                else:
                    # r = mid - 1
                    l = mid + 1
            guard_spots[guard][RIGHT] = smallest

            # Find largest (deepest/rightmost) wall index smaller than (above/left of) guard_y
            wall_indices = wall_cols[guard_y]
            l, r = 0, len(wall_indices) - 1
            largest = -1
            while l <= r:
                mid = (l + r) // 2
                if wall_indices[mid] < guard_x:
                    largest = max(largest, wall_indices[mid])
                    l = mid + 1
                else:
                    r = mid - 1
            guard_spots[guard][UP] = largest

            # Find smallest (shallowest/leftmost) wall index larger than(below/right of) guard_y
            wall_indices = wall_cols[guard_y]
            l, r = 0, len(wall_indices) - 1
            smallest = m
            while l <= r:
                mid = (l + r) // 2
                if wall_indices[mid] > guard_x:
                    smallest = min(smallest, wall_indices[mid])
                    r = mid - 1
                else:
                    l = mid + 1
            guard_spots[guard][DOWN] = smallest
    
        # Now that we know the four "blocking" coordinates for each guard, we can overlap
        # the row and column "range" results together, as intervals, to be able to efficiently
        # query whether an index is covered by a guard or not later on.
        # row_ranges = {i: [] for i in range(m)}
        # col_ranges = {i: [] for j in range(n)}

        # for guard in guard_spots:
        #     left, right, up, down = guard_spots[guard]
        #     row_range = [left, right]
        #     col_range = [up, down]
        # for guard in guard_spots:
        # #print(f"{guard_spots=}")
    
        row_ranges_dict = {i: [] for i in range(m)}
        col_ranges_dict = {j: [] for j in range(n)}
        for guard in guard_spots:
            guard_x, guard_y = guard
            row_ranges_dict[guard_x].append(
                [guard_spots[guard][LEFT], guard_spots[guard][RIGHT]]
            )
            col_ranges_dict[guard_y].append(
                [guard_spots[guard][UP], guard_spots[guard][DOWN]]
            )
        for row in row_ranges_dict:
            row_ranges_dict[row].sort()
        for col in col_ranges_dict:
            col_ranges_dict[col].sort()
        
        #print(f"{row_ranges_dict=}")
        #print(f"{col_ranges_dict=}")

        # Count all positions that are not:
        #   (1) a wall
        #   (2) a guard
        #   (3) in row intersection
        #   (4) in col intersection
        count = 0
        for i in range(m):
            for j in range(n):
                pos = (i, j)
                if pos in walls_set:
                    continue
                if pos in guards_set:
                    continue
                
                is_valid = True

                # Check if a guard can see this position at row 'i'
                # guard_row_ranges = row_ranges_dict[r]
                # for left, right in guard_row_ranges:
                #     if left <= c <= right:
                #         is_valid = False
                #         break
                guard_row_ranges = row_ranges_dict[i]
                l, r = 0, len(guard_row_ranges) - 1
                while l <= r:
                    mid = (l + r) // 2
                    left, right = guard_row_ranges[mid]
                    if left <= j <= right:
                        is_valid = False
                        break
                    elif j < left:
                        r = mid - 1
                    elif j > right:
                        l = mid + 1
                    else:
                        raise Exception("Unreachable case!")
                
                if not is_valid:
                    continue

                # Check if a guard can see this position at col 'j'
                # guard_col_ranges = col_ranges_dict[c]
                # for up, down in guard_col_ranges:
                #     if up <= r <= down:
                #         is_valid = False
                #         break
                guard_col_ranges = col_ranges_dict[j]
                l, r = 0, len(guard_col_ranges) - 1
                while l <= r:
                    mid = (l + r) // 2
                    left, right = guard_col_ranges[mid]
                    if left <= i <= right:
                        is_valid = False
                        break
                    elif i < left:
                        r = mid - 1
                    elif i > right:
                        l = mid + 1
                    else:
                        raise Exception("Unreachable case!")
                    
                if not is_valid:
                    continue
                
                # #print(r, c)
                count += 1
        
        return count



        START, END = 0, 1
        sorted_row_ranges = sorted([
            [guard_spots[guard][LEFT], guard_spots[guard][RIGHT]]
            for guard in guard_spots
        ], key = lambda interval: interval[START])

        sorted_col_ranges = sorted([
            [guard_spots[guard][UP], guard_spots[guard][DOWN]]
            for guard in guard_spots
        ], key = lambda interval: interval[START])
        
        #print()


        row_ranges = [sorted_row_ranges[0]]
        for i in range(1, len(sorted_row_ranges)):
            cur_row_range = sorted_row_ranges[i]
            prev_row_range = row_ranges.pop()

            if prev_row_range[END] < cur_row_range[START]:
                row_ranges.append(prev_row_range)
                row_ranges.append(cur_row_range)
                # continue
            else:
                row_ranges.append(
                    (
                        prev_row_range[START], # guaranteed to be min by sorted order!
                        max(prev_row_range[END], cur_row_range[END])
                    )
                )
        
        col_ranges = [sorted_col_ranges[0]]
        for i in range(1, len(sorted_col_ranges)):
            cur_col_range = sorted_col_ranges[i]
            prev_col_range = col_ranges.pop()

            if prev_col_range[END] < cur_col_range[START]:
                col_ranges.append(prev_col_range)
                col_ranges.append(cur_col_range)
                # continue
            else:
                col_ranges.append(
                    (
                        prev_col_range[START], # guaranteed to be min by sorted order!
                        max(prev_col_range[END], cur_col_range[END])
                    )
                )
        
        #print(f"{row_ranges=}")
        #print(f"{col_ranges=}")

        # for guard in guards:
        #print(f"{guard_spots}")
        return 1


        guards_set = set((row, col) for row, col in guards)
        walls_set = set((row, col) for row, col in walls)
        self.walls_set = walls_set
        self.m, self.n = m, n
        self.finished_moves = set()

        # At beginning, we consider all positions valid, except the ones where
        # we already know there is a guard or a wall.
        # valid_positions = set()
        # for i in range(m):
        #     for j in range(n):
        #         if (i, j) not in guards_set and (i, j) not in walls_set:
        #             # #print((i, j), guards_set)
        #             valid_positions.add((i, j))
        valid_rows = {i: [[0, n - 1]] for i in range(m)}
        valid_cols = {j: [[0, m - 1]] for j in range(n)}
        
        for guard_x, guard_y in guards:
            # Handle row vision first, i.e. left & right directions
            # Binary search to find leftmost & rightmost wall/edge indices
            # the guard can see up to
            
            # Find rightmost wall index to left of guard, or 0 if none
            l, r = 0, guard_x - 1
            rightmost_index = 0
            # while l <= r:

            



            directions = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0)
            ]
            
            for direction in directions:
                dx, dy = direction
                x, y = (guard_x + dx, guard_y + dy)
                
                while self.isValidPosition(x, y) and (x, y, direction) not in self.finished_moves:
                    self.finished_moves.add((x, y, direction))
                    if (x, y) in valid_positions:
                        valid_positions.remove((x, y))
                    x += dx
                    y += dy
        

        # Count all positions that are not:
        #   (1) a wall
        #   (2) a guard
        #   (3) in row intersection
        #   (4) in col intersection
        return len(valid_positions)
