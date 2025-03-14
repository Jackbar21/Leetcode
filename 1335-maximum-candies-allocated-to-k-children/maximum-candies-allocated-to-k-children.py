class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        max_candy = 1
        for candy in candies:
            if max_candy < candy:
                max_candy = candy
        l, r = 1, max_candy
        # Can always give each child 0 candy, but maybe not always max(candies) for each child.
        # Think of this as an array of booleans (0 or more True's followed by 0 or more False's),
        # want to find rightmost 'True' index (i.e. LARGEST VALID value)
        res = 0 # Max candy
        while l <= r:
            mid = (l + r) // 2

            # Can we feed 'mid' amount of candy to each child?
            # Let's see how many children we can feed 'mid' candy
            can_feed = 0
            for candy_count in candies:
                can_feed += candy_count // mid
            
            if can_feed >= k:
                # Valid solution, update res and look for potentially BETTER ONES in right subhalf!
                res = mid
                l = mid + 1
            else:
                # Invalid solution, look for potentially valid ones in left subhalf (giving LESS candy!)
                r = mid - 1
        
        return res
