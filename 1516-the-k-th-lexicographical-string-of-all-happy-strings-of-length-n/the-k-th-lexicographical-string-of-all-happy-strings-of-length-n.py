class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        arr = []
        def backtrack():
            if len(arr) == n:
                yield arr
                return
            
            for char in ["a", "b", "c"]:
                if len(arr) > 0 and arr[-1] == char:
                    continue

                arr.append(char)
                yield from backtrack()
                arr.pop()
            
        res = []
        enumerable = backtrack()
        for _ in range(k):
            try:
                res = next(enumerable)
            except:
                # Not at least k possible happy strings, hence return ""
                return ""
        return "".join(res)