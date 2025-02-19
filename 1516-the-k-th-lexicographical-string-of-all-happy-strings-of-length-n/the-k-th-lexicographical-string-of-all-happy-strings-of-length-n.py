class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        def backtrack():
            if len(res) == n:
                yield "".join(res)
                return
            
            for char in ["a", "b", "c"]:
                if len(res) > 0 and res[-1] == char:
                    continue

                res.append(char)
                yield from backtrack()
                res.pop()
            
        string = ""
        enumerable = backtrack()
        for _ in range(k):
            try:
                string = next(enumerable)
            except:
                # Not at least k possible happy strings, hence return ""
                return ""
        return string