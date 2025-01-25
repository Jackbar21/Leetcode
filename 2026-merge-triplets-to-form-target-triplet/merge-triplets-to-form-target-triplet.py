class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Idea: target == [x, y, z]. 
        #   (1) Grab all the triplets whose x value is <= x
        #   (2) Grab all the triplets whose y value is <= y
        #   (3) Grab all the triplets whose z value is <= z
        #   Get the intersection of these three sets, and figure out if the max
        #   of each three values is indeed x, y, z!
        X, Y, Z = target
        set_x, set_y, set_z = set(), set(), set()
        found_x, found_y, found_z = False, False, False
        for x, y, z in triplets:
            triplet = (x, y, z)
            if x <= X:
                set_x.add(triplet)
                if x == X:
                    found_x = True
            if y <= Y:
                set_y.add(triplet)
                if y == Y:
                    found_y = True
            if z <= Z:
                set_z.add(triplet)
                if z == Z:
                    found_z = True
        
        if not found_x or not found_y or not found_z:
            return False
        
        intersection = (set_x.intersection(set_y)).intersection(set_z)
        max_x, max_y, max_z = 0, 0, 0
        for x, y, z in intersection:
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            if z > max_z:
                max_z = z
        
        return max_x == X and max_y == Y and max_z == Z
