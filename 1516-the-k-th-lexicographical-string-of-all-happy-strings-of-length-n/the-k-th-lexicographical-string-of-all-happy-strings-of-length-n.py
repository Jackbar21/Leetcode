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
            
        arr = list(backtrack())
        print(f"{arr=}")
        return arr[k - 1] if k - 1 < len(arr) else ""