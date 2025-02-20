class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums)
        banned = set(nums)
        
        arr = []
        def backtrack():
            if len(arr) == N:
                yield "".join(arr)
                return
            
            for digit in "01":
                arr.append(digit)
                yield from backtrack()
                arr.pop()
        
        enumerable = backtrack()
        while (bin_string := next(enumerable)) in banned:
            pass
        return bin_string
