class Solution:
    # 1^2 == 1 square of side n
    # 2^2 == 4 sqaures of side (n - 1)
    # 3^2 == 9 squares of side (n - 2)
    # ...
    # n^2      squares of side 1
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    continue

                # matrix[i][j] == 1, so side 1 (i.e. dimension == 1) square valid here!
                count += 1
                max_dimension = min(
                    len(matrix) - i,
                    len(matrix[i]) - j
                )

                # Already handled case where dimension == 1
                for dimension in range(2, max_dimension + 1):
                    offset = dimension - 1
                    is_square = True
                    for index in range(offset + 1):
                        if (matrix[i + index][j + offset] == 0
                            or matrix[i + offset][j + index] == 0
                        ):
                            is_square = False
                            break
                        
                    count += is_square
                    if not is_square:
                        # if n x n square fails, then (n + k) x (n + k)
                        # squares starting from same top-left index, for all k >= 1,
                        # will also be guaranteed to fail. Hence, exit early.
                        break

        return count
                