class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # return self.mergeTripletsNaive(triplets, target)
        TARGET_X, TARGET_Y, TARGET_Z = target
        found_x, found_y, found_z = False, False, False
        for x, y, z in triplets:
            if x > TARGET_X or y > TARGET_Y or z > TARGET_Z:
                continue
            
            if x == TARGET_X:
                found_x = True
            if y == TARGET_Y:
                found_y = True
            if z == TARGET_Z:
                found_z = True

            if found_x and found_y and found_z:
                return True

        return False