class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        chars = []
        # spaces = collections.deque(spaces)
        spaces = spaces[::-1]
        cur_len = 0

        for i, char in enumerate(s):
            if spaces[-1] == i:
                spaces.pop()
                chars.append(" ")
                # Finish the problem early if no spaces left!
                if len(spaces) == 0:
                    return ''.join(chars) + s[i:]
            
            chars.append(char)
        
        return ''.join(chars)