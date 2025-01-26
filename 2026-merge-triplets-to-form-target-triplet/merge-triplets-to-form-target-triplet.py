class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        TARGET_X, TARGET_Y, TARGET_Z = target
        # found_x, found_y, found_z = False, False, False
        max_x, max_y, max_z = 0, 0, 0
        for x, y, z in triplets:
            if x > TARGET_X or y > TARGET_Y or z > TARGET_Z:
                continue
            
            # if x == TARGET_X:
            #     found_x = True
            # if y == TARGET_Y:
            #     found_y = True
            # if z == TARGET_Z:
            #     found_z = True
            # max_x = max(max_x, x)
            # max_y = max(max_y, y)
            # max_z = max(max_z, z)
            if max_x < x:
                max_x = x
            if max_y < y:
                max_y = y
            if max_z < z:
                max_z = z
            
            if max_x == TARGET_X and max_y == TARGET_Y and max_z == TARGET_Z:
                return True

            

            # if found_x and found_y and found_z:
            #     return True

        return False
        return max_x == TARGET_X and max_y == TARGET_Y and max_z == TARGET_Z
