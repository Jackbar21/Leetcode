class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # stack = ['dummy']
        # closed_parentheses = 0
        # open_parentheses = 0
        i = 0
        while i < len(s) and s[i] == ")":
            i += 1
        closed_parentheses = i
        # i = 0
        open_parentheses = 0
        while i < len(s):
            parenthese = s[i]
            if parenthese == "(":
                open_parentheses += 1
            else:
                if open_parentheses > 0:
                    open_parentheses -= 1 # stack.pop()
                else:
                    closed_parentheses += 1 # stack.append(")")
            
            # Loop Invariant
            i += 1
        
        return closed_parentheses + open_parentheses


        for parenthese in s:
            if stack[-1] == "(" and parenthese == ")":
                stack.pop()
            else:
                stack.append(parenthese)

        return len(stack) - 1

        # )))DD))()()()
        #   p