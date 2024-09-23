class Solution:
    def __init__(self):
        self.d = None
        self.s = None
        self.memo = {}
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # return 1
        self.d = dictionary
        self.s = s
        # return 1
        for i in range(len(s)):
            self.memo[(i, i)] = 0 if s[i] in dictionary else 1
        return self.minExtraCharDp(0, len(s) - 1)

        # 10^6

        # (i, j)
        # shortest = sum of (i, k1) + (k1, k2) + ... + (kn, j)
        # (i, j) --> (i, k) + (k, j)
    
    def minExtraCharDp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        # assert i <= j
        # if i == j:
        #     return 0 if self.s[i] in self.d else 1
        assert i < j
            
        
        # O(n) time, where n = len(s)
        if self.s[i:j + 1] in self.d:
            self.memo[(i, j)] = 0
            return 0
        
        # Logic
        # Idea: Find the shortest i-->j k path (similar to Floyd-Warshall algorithm)
        res = j - i + 1
        # TODO: verify if do all correct k indices here
        for k in range(i + 1, j):
        # for k in range(i, j + 1):
            res = min(res, 
                self.minExtraCharDp(i, k - 1) + self.minExtraCharDp(k, j)
            )
        
        # Case 2: just delete first character
        case2 = self.minExtraCharDp(i, i) + self.minExtraCharDp(i + 1, j)
        res = min(res, case2)

        # Case 3: just delete last character
        case3 = self.minExtraCharDp(i, j - 1) + self.minExtraCharDp(j, j)
        res = min(res, case3)
        
        # Return
        self.memo[(i, j)] = res
        return res