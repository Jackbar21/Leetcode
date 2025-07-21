class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        first = second = None
        for third in s:
            if not (first == second == third):
                res.append(third)
            
            first = second
            second = third
        
        return "".join(res)