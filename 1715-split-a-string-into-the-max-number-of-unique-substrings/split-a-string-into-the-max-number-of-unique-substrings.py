class Solution:
    def __init__(self):
        self.s = None
        self.substrings = {} # (i,j) --> s[i : j + 1]
        self.memo = {}
        self.sols = [(set(), 0)]
    def maxUniqueSplit(self, s: str) -> int:
        self.s = s
        # return self.maxUniqueDp([])
        l, r = 0, 0
        return self.maxUniqueSplitDp(set(), l, r)

        # res = self.solve(r)
        # print(sorted(self.sols, key = lambda pair: pair[1], reverse=False))
        # return max(pair[1] for pair in self.sols)
        # hset = self.dp(0, len(self.s) - 1)
        # print(hset)
        # return len(hset)
    
    def dp(self, l, r):
        # Try cutting s at every valid position, i.e. l, l + 1, ..., r
        # including the case where NO CUTS are performed. If not cuts are performed,
        # result is 1, and hence that can be used as base case result value :)
        if (l, r) in self.memo:
            return self.memo[(l, r)]

        # (s[0:1], s[1:])
        # (s[1:2], s[2:])
        # ...
        # (s[1:len(s)], s[len(s):])
        
        # Case where optimal is just to not split l and r anywhere.
        # res = [self.s[l : r + 1]]
        # res = []
        # if l >= r:
        #     return hset
        # hset = set()
        hset = set([self.s[l : r + 1]])
        flag = self.s[l : r + 1] == "bab"

        for split_index in range(l, r):
            left_hset = self.dp(l, split_index)
            right_hset = self.dp(split_index + 1, r)
            if flag:
                print(f"{left_hset=}")
                print(f"{right_hset=}")
            # left = self.dp(l, split_index)
            # left_hset = set(left)
            # if len(left) != len(left_hset):
            #     # print(left, left_hset, "LEFT")
            #     continue

            # right = self.dp(split_index + 1, r)
            # right_hset = set(right)
            # if len(right) != len(right_hset):
            #     # print(right, right_hset, "RIGHT")
            #     continue

            union = left_hset.union(right_hset)
            if len(union) == len(left_hset) + len(right_hset):
                # All substrings unique in left and right, so valid solution!
                # res = max(res, len(union))
                # if len(union) > len(res):
                if len(union) > len(hset):
                    hset = union
                    # res = list(union)
        
        assert len(hset) >= 1
        self.memo[(l, r)] = hset
        return hset
        # assert len(res) >= 1
        self.memo[(l, r)] = res
        return res
                

    
    def solve(self, r):
        if r >= len(self.s):
            return

        new_sols = []
        for hset, l in self.sols:
            substring = self.s[l : r + 1]
            if substring in hset:
                continue
            
            new_sols.append((hset, l))
            hset_copy = hset.copy()
            hset_copy.add(substring)
            new_sols.append((hset_copy, r + 1))

        # for el in new_sols:
        #     self.sols.append(el) 
        self.sols = new_sols
        self.solve(r + 1)
        
        # self.sols = new_sols

    
    def getSubstring(self, l, r):
        # Returns self.s[l : r + 1]
        if (l, r) in self.substrings:
            return self.substrings[(l, r)]
        
        self.substrings[(l, r)] = self.s[l : r + 1]
        return self.substrings[(l, r)]
    
    def maxUniqueSplitDp(self, hset, l, r):
        # if (hset, l, r) in self.memo:
        #     return self.memo[(hset, l, r)]

        # Base Case: r >= len(self.s)
        if r >= len(self.s):
            assert r == len(self.s)
            # substring = self.s[l : r + 1]
            substring = self.getSubstring(l, r)
            # print(f"{substring=}")
            if substring in hset:
                return 0
            if len(substring) > 0:
                hset.add(substring)
            return len(hset)

        # Case 1: Don't split s at index r
        case1 = self.maxUniqueSplitDp(hset.copy(), l, r + 1)

        # Case 2: Split s at index r
        # case2 = self.maxUniqueSplitDp(hset, )
        # substring = self.s[l : r + 1]
        substring = self.getSubstring(l, r)
        case2 = 0
        if substring not in hset:
            # hset_copy = hset.copy()
            hset.add(substring)
            l = r + 1
            r += 1
            case2 = self.maxUniqueSplitDp(hset, l, r)
        
        return max(case1, case2)

        

    
    # def maxUniqueDp(self, bool_arr):
    #     if len(bool_arr) == len(self.s):
    #         return self.solver(bool_arr)
        
    #     # if tuple(bool_arr) in self.memo:
    #     #     return self.memo[tuple(bool_arr)]

    #     # Case 1: Add a 'True', representing that you will split the string at len(bool_arr) index
    #     bool_arr.append(True)
    #     case1 = self.maxUniqueDp(bool_arr.copy())


    #     # Case 2: Add a 'False', representing you will NOT split the string at len(bool_arr) index
    #     # assert bool_arr.pop() == True
    #     bool_arr.pop()
    #     bool_arr.append(False)
    #     case2 = self.maxUniqueDp(bool_arr)

    #     # return case1 + case2
    #     # self.memo[tuple(bool_arr)] = max(case1, case2)
    #     return max(case1, case2)

    # def solver(self, bool_arr):
    #     l, r = 0, 0
    #     arr = set()
    #     assert len(bool_arr) == len(self.s)
        
    #     for split_bool in bool_arr:
    #         if not split_bool:
    #             r += 1
    #             continue
            
    #         # substring = None
    #         # if (l, r) in self.substrings:
    #         #     substring = self.substrings[(l, r)]
    #         # else:
    #         #     substring = self.s[l : r + 1]
    #         #     self.substrings[(l, r)] = substring
    #         # substring = self.s[l : r + 1]

    #         # substring = self.substrings.get((l, r), self.s[l : r + 1])
    #         # self.substrings[(l, r)] = substring
    #         substring = self.s[l : r + 1]

    #         # Invalid, so return 0
    #         if substring in arr:
    #             return 0 # Invalid!

    #         arr.add(substring)
    #         r += 1
    #         l = r

    #     # Valid, so return len(arr) [or count of "True" inside boolean array] as answer
    #     return len(arr)

