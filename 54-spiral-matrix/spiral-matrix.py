class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
        inBounds = lambda x, y: 0 <= x < M and 0 <= y < N

        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)] # RIGHT, DOWN, LEFT, UP
        direction_index = 0
        
        i, j = 0, 0
        visited = set([(i, j)])
        res = [matrix[i][j]]
        while len(visited) < M * N:
            di, dj = DIRECTIONS[direction_index]
            next_i, next_j = i + di, j + dj
            if not inBounds(next_i, next_j) or (next_i, next_j) in visited:
                direction_index = (direction_index + 1) % len(DIRECTIONS)
                continue

            i, j = next_i, next_j
            visited.add((i, j))
            res.append(matrix[i][j])
        
        return res
        return [matrix[i][j] for i, j in visited]

