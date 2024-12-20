class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = []
        self.backtrackNaive(0, [])
        return list(set(self.res))
    
    def backtrackNaive(self, i, res):
        # Base Case
        if i >= len(self.nums):
            self.res.append(tuple(sorted(res)))
            return

        # Either choose to include num at index i or not :)
        # Case 1: Include num
        num = self.nums[i]
        res.append(num)
        self.backtrackNaive(i + 1, res)
        res.pop()

        # Case 2: Don't include num
        self.backtrackNaive(i + 1, res)

    # def backtrack(self, i: int, res: list, used: set) -> None:
