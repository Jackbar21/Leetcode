class Solution:
    def __init__(self):
        self.expression = None
        self.open_to_close = {} # mappings of open-to-closed parenthese index pairs
        self.parenthese_index = -1
    def getClosingParentheseIndex(self, open_parenthese_index):
        # assert open_parenthese_index < len(self.expression)
        # assert self.expression[open_parenthese_index] == "("
        # assert open_parenthese_index in self.open_to_close
        return self.open_to_close[open_parenthese_index]

    def parseBoolExpr(self, expression: str) -> bool:
        # Pre-Populate all open-to-closed parenthese index pairs.
        # This is done in O(n) time, and allows for quick O(1)
        # lookup of open parenthese to matching closing parenthese pairs.
        stack = [] # indices of open parenthese characters
        for i, char in enumerate(expression):
            if char == "(":
                stack.append(i)
            elif char == ")":
                # assert len(stack) > 0
                open_parenthese_index = stack.pop()
                # assert open_parenthese_index not in self.open_to_close
                self.open_to_close[open_parenthese_index] = i
        
        self.expression = expression
        return self.parseBoolExprHelper(0, len(expression) - 1)
    
    def parseBoolExprHelper(self, l, r):
        # Case 1: Just boolean value (must be ONLY one index!)
        if l >= r or self.expression[l] in ["f", "t"]:
            # assert l == r and self.expression[l] in ["f", "t"]
            return self.expression[l] == "t"

        logical_symbol = self.expression[l]
        # assert logical_symbol in ["!", "&", "|"]
        open_parenthese_index = l + 1
        closed_parenthese_index = self.getClosingParentheseIndex(open_parenthese_index)
        left, right = open_parenthese_index + 1, closed_parenthese_index - 1
        # assert left <= right < len(self.expression)

        # Case 2: Negation - !(...)
        if logical_symbol == "!":
            return not self.parseBoolExprHelper(left, right)

        # Case 3: Logical And - &(...)
        if logical_symbol == "&":
            return self.logical_and(left, right)

        # Case 4: Logical Or - |(...)
        # assert logical_symbol == "|"
        return self.logical_or(left, right)
    
    def logical_and(self, l, r):
        # Base Case: End of string
        if l >= r:
            # assert l == r and self.expression[l] in ["f", "t", ")"]
            return self.expression[l] != "f"
        
        # Case 1: Just boolean value (must be ONLY one index!)
        if self.expression[l] in ["f", "t"]:
            if self.expression[l] == "f":
                return False
            
            # assert l + 2 <= r
            return self.logical_and(l + 2, r)
        
        # Case 2: Logical Operation
        logical_symbol = self.expression[l]
        # assert logical_symbol in ["!", "&", "|"]
        open_parenthese_index = l + 1
        closed_parenthese_index = self.getClosingParentheseIndex(open_parenthese_index)
        left, right = open_parenthese_index + 1, closed_parenthese_index - 1
        # assert left <= right < len(self.expression)

        if logical_symbol == "!":
            expr = not self.parseBoolExprHelper(left, right)
            if expr == False:
                return False
        
        elif logical_symbol == "&":
            expr = self.logical_and(left, right)
            if expr == False:
                return False
        
        else:
            assert logical_symbol == "|"
            expr = self.logical_or(left, right)
            if expr == False:
                return False

        # Expression was valid, so update l (and be careful not to overshoot!), 
        # then compute rest of logical_and operation :)
        l = min(closed_parenthese_index + 2, r)
        return self.logical_and(l, r)
        

        # # Base Case: 
        # if l >= r or self.expression[l] in ["f", "t"]:
        #     # assert l == r and self.expression[l] in ["f", "t"]
        #     if self.expression[l] == "f":
        #         return False

        # logical_symbol = self.expression[l]
        # # assert logical_symbol in ["!", "&", "|"]

        # # Regardless of what logical_symbol is, we must find where the closing parenthese is
        # # We can do this by keeping track of a stack of open parentheses (and popping whenever
        # # we see matching closing parenthese) until we see there are 0 parentheses left!
        # stack = ["("]
        # index = l + 2 # since l + 1 is index of opening parenthese
        # while len(stack) > 0:
        #     # assert index < len(self.expression)
        #     if self.expression[index] == "(":
        #         stack.append("(")
        #     elif self.expression[index] == ")":
        #         stack.pop()
        #     index += 1
        # # Rightmost closing parenthese is at index - 1. So want to evaluate sub-expression
        # # from l + 2 to index - 2


        # # l += 2
        # # r -= 1
        # # assert l <= r
        # # Case 2: Negation - !(...)
        # # if logical_symbol == "!":




        # # Case 3: Logical And - &(...)

        # # Case 4: Logical Or - |(...)

        # return res

        # # f,f,t,|(f,f,t),t,f
    
    def logical_or(self, l, r):
        # assert l <= r < len(self.expression)

        # print(self.expression[l:r + 1])
        
        # Base Case: end of string
        if l >= r:
            # assert l == r # might be better to do l = min(l, r) in case I overshoot due to ','
            # assert self.expression[l] in ["f", "t", ")"]
            # if self.expression[l] == ")":
                # print("GIGA ALERT MODE!!!")
            # print("ALERT", self.expression[l])
            # return self.expression[l] != "f" # TODO: might need to double check this...
            return self.expression[l] == "t"
        
        # Case 1: Just boolean value (must be ONLY one index!)
        if self.expression[l] in ["f", "t"]:
            if self.expression[l] == "t":
                return True
            
            # assert l + 2 <= r
            return self.logical_or(l + 2, r)
        
        # Case 2: Logical Operation
        logical_symbol = self.expression[l]
        # assert logical_symbol in ["!", "&", "|"]
        open_parenthese_index = l + 1
        closed_parenthese_index = self.getClosingParentheseIndex(open_parenthese_index)
        left, right = open_parenthese_index + 1, closed_parenthese_index - 1
        # assert left <= right < len(self.expression)

        if logical_symbol == "!":
            expr = not self.parseBoolExprHelper(left, right)
            if expr == True:
                return True
        
        elif logical_symbol == "&":
            expr = self.logical_and(left, right)
            if expr == True:
                return True
        
        elif logical_symbol == "|":
            expr = self.logical_or(left, right)
            if expr == True:
                return True

        else:
            raise Exception("Unreachable Code")

        # Expression was valid, so update l (and be careful not to overshoot!), 
        # then compute rest of logical_and operation :)
        l = min(closed_parenthese_index + 2, r)
        return self.logical_or(l, r)