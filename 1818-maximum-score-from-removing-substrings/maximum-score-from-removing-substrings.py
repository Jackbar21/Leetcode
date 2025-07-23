class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        return self.xHelper(s, x, y) if x >= y else self.yHelper(s, x, y)
    
    def xHelper(self, s, x, y):
        res = 0

        # Handle x first
        stack = [None]
        for letter in s:
            if stack[-1] == "a" and letter == "b":
                stack.pop()
                res += x
            else:
                stack.append(letter)
        
        # Handle y second
        s = "".join(letter for letter in stack[1:])
        stack = [None]
        for letter in s:
            if stack[-1] == "b" and letter == "a":
                stack.pop()
                res += y
            else:
                stack.append(letter)
        
        return res
    
    def yHelper(self, s, x, y):
        res = 0

        # Handle y first
        stack = [None]
        for letter in s:
            if stack[-1] == "b" and letter == "a":
                stack.pop()
                res += y
            else:
                stack.append(letter)
        
        # Handle x second
        s = "".join(letter for letter in stack[1:])
        stack = [None]
        for letter in s:
            if stack[-1] == "a" and letter == "b":
                stack.pop()
                res += x
            else:
                stack.append(letter)
        
        return res
