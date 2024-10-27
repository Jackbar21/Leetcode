class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    continue
                
                
                max_dimension = min(
                    len(matrix) - i,
                    len(matrix[i]) - j
                )

                count += 1 # matrix[i][j] == 1, so side 1 square valid here!
                # Already handled case where dimension == 1
                for dimension in range(2, max_dimension + 1):
                    offset = dimension - 1
                    is_square = True
                    for index in range(offset + 1):
                        if matrix[i + index][j + offset] == 0:
                            is_square = False
                            break
                        if matrix[i + offset][j + index] == 0:
                            is_square = False
                            break
                        
                    count += is_square
                    if not is_square:
                        break

        return count
                