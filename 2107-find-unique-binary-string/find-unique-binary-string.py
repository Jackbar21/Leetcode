class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums)
        banned = set(nums)
        
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
        
        enumerable = list(backtrack())
        # print(f"{enumerable}")
        return enumerable[random.randint(0, len(enumerable) - 1)]
        while (bin_string := next(enumerable)) in banned:
            pass
        return bin_string
