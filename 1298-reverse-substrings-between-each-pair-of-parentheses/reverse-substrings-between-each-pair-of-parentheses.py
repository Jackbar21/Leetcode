class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for i, letter in enumerate(s):
            if letter != ')':
                stack.append(letter)
                continue
            
            # ')' found, so reverse entire current string from
            # first '(' popped, which of course is innermost one
            tmp = []
            while stack[-1] != '(':
                tmp.append(stack.pop())

            stack.pop() # '(' parenthese
            stack += tmp
    
        return ''.join(stack)
