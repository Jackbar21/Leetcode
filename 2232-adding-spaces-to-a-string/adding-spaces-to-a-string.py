class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        chars = []
        spaces = collections.deque(spaces)
        cur_len = 0

        for i, char in enumerate(s):
            if len(spaces) > 0 and spaces[0] == i:
                spaces.popleft()
                chars.append(" ")
            
            chars.append(char)
        
        return ''.join(chars)