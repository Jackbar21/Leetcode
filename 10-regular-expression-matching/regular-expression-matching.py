class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.s, self.p = s, p
        self.memo = {}
        return self.dp(0, 0)
    
    def dp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        N, M = len(self.s), len(self.p)
        # i represents current index in input string 's'
        # j represents current index in pattern str. 'p'

        if i >= N:
            # Not allowed to add anymore characters. Hence, it must be that
            # either 'p' is also exhausted, or followed by a sequence of 
            # one or more '<char>*' patterns, where <char> is any character including '.'
            while j < M:
                if not (j + 1 < M and self.p[j + 1] == "*"):
                    self.memo[(i, j)] = False
                    return False
                j += 2
            self.memo[(i, j)] = True
            return True  
        elif j >= M:
            self.memo[(i, j)] = False
            return False
        
        letter_s, letter_p = self.s[i], self.p[j]
        
        # Case 1: index j + 1 maps to a '*'
        if (j + 1) < M and self.p[j + 1] == "*":
            # Can select 0 or more instances of letter_p to match with s
            next_j_index = j + 2

            # Case 1(a): Pick 0 letters
            if self.dp(i, next_j_index):
                self.memo[(i, j)] = True
                return True
            
            # Case 1(b): Pick 1 or more letters
            index = i
            while index < N and (self.s[index] == letter_p or letter_p == "."):
                if self.dp(index + 1, next_j_index):
                    self.memo[(i, j)] = True
                    return True
                index += 1
        
        # Case 2: index j + 1 does not map to '*', which is simplest case
        self.memo[(i, j)] = (letter_s == letter_p or letter_p == ".") and self.dp(i + 1, j + 1)
        return self.memo[(i, j)]
