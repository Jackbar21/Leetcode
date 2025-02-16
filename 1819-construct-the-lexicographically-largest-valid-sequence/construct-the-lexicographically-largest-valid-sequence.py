class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # Idea: Do things in terms of available indices. For instance, for any n,
        # we have 1 + 2*(n-1) available indices. Whenever you want to grab an index
        # for a number 'num', it must be that index and index + num are both available,
        # then keep backtracking, etc etc... You will have to remember a number's chosen
        # indices probably, but that shouldn't be too much of an issue w/ a dictionary :)
        self.largest = []
        self.available_indices = set(range(2*n - 1))
        self.d = {} # num to indices
        
        def backtrack():
            if len(self.available_indices) == 0:
                res = [0] * (2*n - 1)
                for num, indices in self.d.items():
                    for index in indices:
                        res[index] = num
                if res > self.largest:
                    self.largest = res.copy()
                return True
            
            # We need to fill in EVERY available index, so we might as well figure out largest
            # number we can put in SMALLEST available index, as that will have the LARGEST impact
            # on how "lexicographically large" our result will be!
            index = min(self.available_indices)
            for num in range(n, 0, -1):
                if num in self.d:
                    # Already paired this number with indices, so ignore it!
                    continue

                # Special case, as only takes up ONE index!
                if num == 1:
                    self.d[num] = (index,)
                    self.available_indices.remove(index)

                    if backtrack():
                        return True
        
                    del self.d[num]
                    self.available_indices.add(index)
                    continue

                # Not even worth trying index, as other needed index isn't even available!
                if (index + num) not in self.available_indices:
                    continue
                
                # Otherwise, try the index and see if it works!
                self.d[num] = (index, index + num)
                self.available_indices.remove(index)
                self.available_indices.remove(index + num)

                if backtrack():
                    return True

                del self.d[num]
                self.available_indices.add(index)
                self.available_indices.add(index + num)

            return False

        # Problem statement GUARANTEES a solution exists!
        backtrack()
        return self.largest   
