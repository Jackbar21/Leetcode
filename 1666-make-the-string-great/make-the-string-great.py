class Solution:
    def makeGood(self, s: str) -> str:
        stack = deque()
        stack.append("@")

        for c in s:
            prev_c = stack[-1]
            if c == prev_c.upper() or c == prev_c.lower():
                if c != prev_c:
                    stack.pop()
                    continue
            stack.append(c)
        
        stack.popleft()
        return "".join(stack)
