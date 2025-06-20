class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        NORTH, SOUTH, EAST, WEST = "N", "S", "E", "W"
        DIRECTIONS = [NORTH, SOUTH, EAST, WEST]
        combinations = [
            (NORTH, EAST),
            (NORTH, WEST),
            (SOUTH, EAST),
            (SOUTH, WEST)
        ]

        res = 0
        for y_direction, x_direction in combinations:
            changed = 0
            dist = 0
            for direction in s:

                if direction == y_direction or direction == x_direction:
                    dist += 1
                    continue
                elif changed < k:
                    changed += 1
                    dist += 1
                else:
                    # Gotta move in an UNWANTED direction, and can't
                    # change any more directions, so this will HURT current score.
                    # However, since problems asks for maximum Manhatten distance
                    # reached at ANY time, not ONLY after going through entire string s,
                    # we update res here if smaller than current 'dist'.
                    if res < dist:
                        res = dist
                    dist -= 1 
            
            if res < dist:
                res = dist
        
        return res
