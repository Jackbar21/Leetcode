class Solution:
    def __init__(self):
        self.s = None
        self.substrings = {} # (i,j) --> s[i : j + 1]
    def maxUniqueSplit(self, s: str) -> int:
        self.s = s
        return self.maxUniqueDp([])
    
    def maxUniqueDp(self, bool_arr):
        if len(bool_arr) == len(self.s):
            return self.solver(bool_arr)

        # Case 1: Add a 'True', representing that you will split the string at len(bool_arr) index
        bool_arr.append(True)
        case1 = self.maxUniqueDp(bool_arr.copy())


        # Case 2: Add a 'False', representing you will NOT split the string at len(bool_arr) index
        # assert bool_arr.pop() == True
        bool_arr.pop()
        bool_arr.append(False)
        case2 = self.maxUniqueDp(bool_arr)

        # return case1 + case2
        return max(case1, case2)

    def solver(self, bool_arr):
        l, r = 0, 0
        arr = set()
        assert len(bool_arr) == len(self.s)
        
        for split_bool in bool_arr:
            if not split_bool:
                r += 1
                continue
            
            # substring = None
            # if (l, r) in self.substrings:
            #     substring = self.substrings[(l, r)]
            # else:
            #     substring = self.s[l : r + 1]
            #     self.substrings[(l, r)] = substring
            # substring = self.s[l : r + 1]
            substring = self.substrings.get((l, r), self.s[l : r + 1])
            self.substrings[(l, r)] = substring

            # Invalid, so return 0
            if substring in arr:
                return 0 # Invalid!

            arr.add(substring)
            r += 1
            l = r

        # Valid, so return len(arr) [or count of "True" inside boolean array] as answer
        return len(arr)

