class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        cur = []
        for letter in s:
            if len(cur) < k:
                cur.append(letter)
            else:
                assert len(cur) == k
                res.append("".join(cur))
                cur = [letter]
        
        res.append("".join(cur) + fill * (k - len(cur)))
        return res
