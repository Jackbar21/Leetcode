class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]

        for i in range(1,len(s)):
            letter = s[i]
            if stack and stack[-1] != letter and stack[-1].lower() == letter.lower():
                stack.pop()
            else:
                stack.append(letter)
        
        return ''.join(stack)
