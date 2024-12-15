class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # ORIGINAL (MY) SOLUTION:
        res = [[]]
        for num in nums:
            new_res = []
            for lst in res:
                new_lst = lst.copy()
                new_lst.append(num)
                new_res.append(new_lst)
            res.extend(new_res)
        return res

        # BACKTRACKING SOLUTION (FROM NEETCODE - FOR LEARNING PURPOSES!):
        # res = []
        # subset = []
        # def backtrack(i):
        #     # Base case:
        #     if i >= len(nums):
        #         # We have found a subset, where for each index i in num, we either
        #         # chose to include (or not include) it in our current subset! Each of
        #         # these cases will be unique, and once per 2^n total unique solutions!
        #         res.append(subset.copy())
        #         return

        #     # Case 1: Include num at index i
        #     subset.append(nums[i])
        #     backtrack(i + 1)

        #     # Case 2: Don't include num at index i
        #     subset.pop()
        #     backtrack(i + 1)
        
        # backtrack(0)
        # return res