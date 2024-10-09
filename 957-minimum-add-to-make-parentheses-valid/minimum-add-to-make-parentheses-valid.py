class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_parentheses, closed_parentheses = 0, 0
        for parenthese in s:
            if parenthese == "(":
                open_parentheses += 1
            # elif open_parentheses > 0:
            #     open_parentheses -= 1
            # else:
            #     closed_parentheses += 1
            else:
                closed_parentheses += open_parentheses == 0
                open_parentheses -= open_parentheses > 0 
        
        return closed_parentheses + open_parentheses