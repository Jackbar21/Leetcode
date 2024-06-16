class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) <= 0:
            return False
        
        r, c = 0, len(matrix[0]) - 1
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            elif target > matrix[r][c]:
                r += 1
            else:
                # target < matrix[r][c]
                c -= 1
        return False