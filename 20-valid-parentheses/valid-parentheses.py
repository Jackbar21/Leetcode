class Solution:
    def isValid(self, s: str) -> bool:
        # Idea: whenever add opening parenthese, it must be
        # eventually closed. To prevent cases such as:
        #       "([)]"
        # We need to be careful in that only the innermost open
        # parenthese can be closed, for which we may use a stack
        # datastructure. We allow only the current "innermost"
        # parenthese to be closed (which will be at the top of
        # the stack), and if at any point that heuristic isn't
        # satisfied, we know the string is invalid. Otherwise,
        # we know the string is valid if and only if the stack is 
        # empty (since otherwise not all parentheses were closed), 
        # and can return as such.

        stack = []

        open_to_closed = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        
        open_parentheses = open_to_closed.keys()

        closed_to_open = {value: key for key, value in open_to_closed.items()}
        closed_parentheses = closed_to_open.keys()

        for parenthese in s:
            print(parenthese)
            if parenthese in open_parentheses:
                stack.append(parenthese)
            else:
                open_parenthese = closed_to_open[parenthese]
                if len(stack) == 0 or stack[-1] != open_parenthese:
                    return False
                stack.pop()
        
        return len(stack) == 0
