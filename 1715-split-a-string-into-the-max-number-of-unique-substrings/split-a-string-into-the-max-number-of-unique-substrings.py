class Solution:
    def __init__(self):
        self.s = None
    def maxUniqueSplit(self, s: str) -> int:
        # num_splits = [False] * (len(s) - 1)
        self.s = s
        return self.maxUniqueDp([])
    
    def maxUniqueDp(self, bool_arr):
        if len(bool_arr) == len(self.s):
            return self.solver(bool_arr)

        # Case 1: Add a 'True', representing that you will split the string at len(bool_arr) index
        bool_arr.append(True)
        case1 = self.maxUniqueDp(bool_arr.copy())


        # Case 2: Add a 'False', representing you will NOT split the string at len(bool_arr) index
        # print(bool_arr)
        assert bool_arr.pop() == True
        bool_arr.append(False)
        case2 = self.maxUniqueDp(bool_arr.copy())

        # return case1 + case2
        return max(case1, case2)

    def solver(self, bool_arr):
        assert len(bool_arr) == len(self.s)

        l = 0
        r = 0

        arr = []

        for split_bool in bool_arr:
            if not split_bool:
                r += 1
                continue
            
            arr.append(self.s[l : r + 1])
            r += 1
            l = r
            # l = r + 1
        
        # Valid, so return len(arr) [or count of "True" inside boolean array] as answer
        if len(arr) == len(set(arr)):
        #     return len(arr)
            return bool_arr.count(True)
        
        # Invalid, so return 0
        return 0

