class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        cur = []
        for letter in s:
            if len(cur) == k:
                res.append("".join(cur))
                cur = []
            
            cur.append(letter)
        
        res.append("".join(cur) + fill * (k - len(cur)))
        return res
