class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # return self.naive(n) # Too Slow!

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

# [2,1,3,4,5,6,7,8,9] >>> [1,9,8,7,6,5,4,3,2] 
    
    def naive(self, n):
        self.res = []
        self.largest = []

        

        # self.global_dict = {num: 2 for num in range(2, n + 1)} # at most 20 keys!
        # self.global_dict[1] = 1
        self.global_dict = [0,1] + [2]*(n-1)
        def backtrack():
            # print()
            # print(f"{self.res=}")
            # print(f"{self.global_dict=}")
            # d = {key: val for key, val in self.global_dict.items() if val > 0}
            sorted_keys = [num for num in range(n, -1, -1) if self.global_dict[num] > 0]
            # print(f"{d=}")
            if len(sorted_keys) == 0:
                # print(f"{self.res=}, {self.largest=}")
                if self.res > self.largest:
                    self.largest = [el for el in self.res]
                return True
                # return

            # if num == 1:
            #     self.res.append(1)
            #     assert len(self.res) == 2*n - 1
            #     if self.res > self.largest:
            #         # self.largest = self.res.copy()
            #         self.largest = [el for el in self.res]
            #     self.res.pop()
            #     return True
            
            # sorted_keys = sorted(d.keys(), reverse=True)
            # print(f"{sorted_keys=}")
            for num in sorted_keys:
                # If num is not 1, then the value in global_dict should have been 2.
                # However, if the value is not 2, that means this is the SECOND time we
                # select this number! In that case, it should be that the index at 
                # len(self.res) - num is not only well defined, but ALSO be EXACTLY the
                # SAME value!
                if num != 1 and self.global_dict[num] != 2:
                    index = len(self.res) - num
                    if index < 0 or self.res[index] != num:
                        continue
                
                # Try adding number here!
                self.res.append(num)
                self.global_dict[num] -= 1

                success = backtrack()

                self.res.pop()
                self.global_dict[num] += 1

                # If successful, don't try anything else here, as it is
                # guaranteed to be lexicographically smaller!
                if success:
                    return True
            
            # No number available to us worked, so this is a "dead end"
            return False
        
        assert backtrack()
        return self.largest