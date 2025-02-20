class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums)
        banned = (nums)
        
        arr = []
        def backtrack():
            if len(arr) == N:
                bin_string = "".join(arr)
                if bin_string not in banned:
                    yield bin_string
                return
            
            for digit in "01":
                arr.append(digit)
                yield from backtrack()
                arr.pop()
        
        valid_solutions = backtrack() # Enumerable of ALL valid solutions
        return next(valid_solutions) # Return first result!
