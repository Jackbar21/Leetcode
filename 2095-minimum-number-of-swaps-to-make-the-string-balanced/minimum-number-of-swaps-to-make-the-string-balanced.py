class Solution:
    def minSwaps(self, s: str) -> int:
        stack = collections.deque(['dummy'])
        for bracket in s:
            if stack[-1] == "[" and bracket == "]":
                stack.pop()
            else:
                stack.append(bracket)
        stack.popleft()

        return math.ceil(len(stack) / 4)
