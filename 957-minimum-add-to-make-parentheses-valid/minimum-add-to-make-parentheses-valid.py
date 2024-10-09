class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = ['dummy']
        for parenthese in s:
            if stack[-1] == "(" and parenthese == ")":
                stack.pop()
            else:
                stack.append(parenthese)
        
        # print(''.join(stack[1:]))
        # return -1

        return len(stack) - 1

        # ))))))(

        # () --> 0
        # (( --> 2
        # ))))))
        # )(

        # ))...)) ((...((