class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        return self.mergeTripletsNaive(triplets, target)
    
    def mergeTripletsNaive(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Idea: target == [x, y, z]. 
        #   (1) Grab all the triplets whose x value is <= x
        #   (2) Grab all the triplets whose y value is <= y
        #   (3) Grab all the triplets whose z value is <= z
        #   Get the intersection of these three sets, and figure out if the max
        #   of each three values is indeed x, y, z!
        X, Y, Z = target
        set_x, set_y, set_z = set(), set(), set()
        for x, y, z in triplets:
            triplet = (x, y, z)
            if x <= X:
                set_x.add(triplet)
            if y <= Y:
                set_y.add(triplet)
            if z <= Z:
                set_z.add(triplet)
        
        set1, set2, set3 = sorted([set_x, set_y, set_z], key=len)
        intersection = [triplet for triplet in set1 if triplet in set2 and triplet in set3]
        found_x, found_y, found_z = False, False, False
        for x, y, z in intersection:
            if x == X:
                found_x = True
            if y == Y:
                found_y = True
            if z == Z:
                found_z = True
            if found_x and found_y and found_z:
                return True
            
        return False
