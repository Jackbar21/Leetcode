class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for parenthese in s:
            if parenthese in "({[":
                stack.append(parenthese)
            else:
                if len(stack) == 0 or stack[-1] != closed_to_open[parenthese]:
                    return False
                stack.pop()

        return len(stack) == 0