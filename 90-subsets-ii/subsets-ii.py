class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = set()
        self.backtrack(0, [])
        return list(self.res)
    
    def backtrack(self, i: int, res: list) -> None:
        # Base Case
        if i >= len(self.nums):
            self.res.add(tuple(sorted(res)))
            return

        # Either choose to include num at index i or not :)
        # Case 1: Include num
        res.append(self.nums[i])
        self.backtrack(i + 1, res)
        res.pop()

        # Case 2: Don't include num
        self.backtrack(i + 1, res)
