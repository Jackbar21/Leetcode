class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                stack.append(-stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                l, r = stack.pop(), stack.pop()
                stack.append(int(r / l))
            else:
                stack.append(int(token))
        
        return stack.pop()