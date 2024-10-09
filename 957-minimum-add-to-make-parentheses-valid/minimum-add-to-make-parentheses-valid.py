class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # stack = ['dummy']
        # closed_parentheses = 0
        # open_parentheses = 0
        i = 0
        # while i < len(s) and s[i] == ")":
        #     i += 1
        # closed_parentheses = i
        # # i = 0
        # open_parentheses = 0
        # while i < len(s):
        open_parentheses, closed_parentheses = 0, 0
        for parenthese in s:
            if parenthese == "(":
                open_parentheses += 1
            else:
                if open_parentheses > 0:
                    open_parentheses -= 1 # stack.pop()
                else:
                    closed_parentheses += 1 # stack.append(")")
        
        return closed_parentheses + open_parentheses