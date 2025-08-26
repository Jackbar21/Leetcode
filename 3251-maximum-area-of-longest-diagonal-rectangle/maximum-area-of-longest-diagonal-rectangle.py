class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        max_area = 0
        for length, width in dimensions:
            diagonal = length * length + width * width # No need to sqrt for comparison checks :)
            area = length * width
            if diagonal > max_diagonal:
                max_diagonal = diagonal
                max_area = area
            elif diagonal == max_diagonal and max_area < area:
                max_area = area
        return max_area
