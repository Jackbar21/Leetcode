class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Loop through nums in REVERSE order, until you reach the FIRST
        # index i that is maps to a duplicate number! Then you know you
        # must delete EVERY element in nums[0..i], deleting 3 elements
        # at a time, with a total of i - 0 + 1 == i + 1 elements.
        # Hence, given this index i, minimum number of operations
        # will simply be math.ceil((i + 1) / 3)
        seen = set()
        index = None
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if num in seen:
                index = i
                break
            seen.add(num)
        
        return 0 if index is None else math.ceil((i + 1) / 3)
