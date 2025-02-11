class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        N = len(part)
        stack = []
        for letter in s:
            stack.append(letter)
            if len(stack) >= N and "".join(stack[-N:]) == part:
                stack = stack[:-N]
        return "".join(stack)