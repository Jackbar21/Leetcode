class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) <= 0:
            return 0
        
        letters = [letter.upper() for letter in 'ivxlcdm']
        values = [1,5,10,50,100,500,1000]
        assert len(letters) == len(values)
        d = {
            letters[i]: values[i] for i in range(len(values))
        }

        if len(s) == 1:
            return d[s[0]]
        
        if s[0] == 'I':
            if s[1] == 'V':
                return 4 + self.romanToInt(s[2:])
            if s[1] == 'X':
                return 9 + self.romanToInt(s[2:])
        
        if s[0] == 'X':
            if s[1] == 'L':
                return 40 + self.romanToInt(s[2:])
            if s[1] == 'C':
                return 90 + self.romanToInt(s[2:])
        
        if s[0] == 'C':
            if s[1] == 'D':
                return 400 + self.romanToInt(s[2:])
            if s[1] == 'M':
                return 900 + self.romanToInt(s[2:])
        
        return d[s[0]] + self.romanToInt(s[1:])