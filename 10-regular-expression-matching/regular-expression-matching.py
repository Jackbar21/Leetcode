class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.s, self.p = s, p
        return self.dp(0, 0)
    
    @cache
    def dp(self, i, j):
        # i represents current index in input string 's'
        # j represents current index in pattern str. 'p'
        print(f"{i=}, {j=}")

        if i >= len(self.s):
            # Not allowed to add anymore characters. Hence, it must be that
            # either 'p' is also exhausted, or followed by a sequence of 
            # one or more '<char>*' patterns, where <char> is any character including '.'
            # if j >= len(self.p):
            #     return True
            
            while j < len(self.p):
                if not (j + 1 < len(self.p) and self.p[j + 1] == "*"):
                    return False
                j += 2
            return True
            
        
        if j >= len(self.p):
            assert i < len(self.s)
            return False
        
        letter_s, letter_p = self.s[i], self.p[j]
        
        # Case 1: index j + 1 maps to a '*'
        print(f"{(j + 1) < len(self.p)=}")
        if (j + 1) < len(self.p):
            print(f"{self.p[j + 1] == '*'=}")
        if (j + 1) < len(self.p) and self.p[j + 1] == "*":
            print(f"TRUE")
            # if letter_p == ".":
            #     return True

            # Can select 0 or more instances of letter_p to match with s
            next_j_index = j + 2

            # Case 1: Pick 0 letters
            if self.dp(i, next_j_index):
                return True
            
            index = i
            while index < len(self.s) and (self.s[index] == letter_p or letter_p == "."):
                if self.dp(index + 1, next_j_index):
                    return True
                index += 1
                # if index >= len(self.s):
                #     return True

        
        if letter_p == ".":
            return self.dp(i + 1, j + 1)
        
        return (letter_s == letter_p) and self.dp(i + 1, j + 1)