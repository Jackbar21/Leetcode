class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        arr = []
        self.count = 0
        self.res = "" # Default if no solution is found!
        def backtrack():
            if len(arr) == n:
                self.count += 1
                if self.count == k:
                    # Found k'th lexicographically smallest string, so set
                    # as global solution result!
                    self.res = "".join(arr)
                return
            
            # If found solution, then stop!
            if self.count >= k:
                return
            
            prev_char = arr[-1] if len(arr) > 0 else None
            for char in ["a", "b", "c"]:
                if char == prev_char:
                    continue

                arr.append(char)
                backtrack()
                arr.pop()
        
        backtrack()
        return self.res

    
    def yielding(self, n: int, k: int) -> str:
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