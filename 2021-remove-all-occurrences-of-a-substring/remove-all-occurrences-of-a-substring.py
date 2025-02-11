class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        N = len(part)
        part_hash = hash(part)
        stack = []
        for letter in s:
            stack.append(letter)
            if len(stack) >= N and hash("".join(stack[-N:])) == part_hash:
                for _ in range(N):
                    stack.pop()
        return "".join(stack)