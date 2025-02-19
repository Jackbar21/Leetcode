class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        arr = []
        def backtrack():
            if len(arr) == n:
                yield arr
                return
            
            prev_char = arr[-1] if len(arr) > 0 else None
            for char in ["a", "b", "c"]:
                if char == prev_char:
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