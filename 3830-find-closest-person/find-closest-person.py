class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        return 1 if (delta_x := abs(z - x)) < (delta_y := abs(z - y)) else 2 if delta_y < delta_x else 0