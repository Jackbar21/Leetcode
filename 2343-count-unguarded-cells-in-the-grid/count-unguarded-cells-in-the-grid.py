class Solution:
    def isValidPosition(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n and (x, y) not in self.walls_set
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guards_set = set((row, col) for row, col in guards)
        walls_set = set((row, col) for row, col in walls)
        self.walls_set = walls_set
        self.m, self.n = m, n
        self.finished_moves = set()

        # At beginning, we consider all positions valid, except the ones where
        # we already know there is a guard or a wall.
        valid_positions = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in guards_set and (i, j) not in walls_set:
                    valid_positions.add((i, j))

        for guard_x, guard_y in guards:
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
        
        return len(valid_positions)
