class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = []
        # if len(nums) == 1:
        #     return [[nums[0]]] # TODO: Might need to do nums.copy() ?

        # nums_set = set(nums)
        # d = {}
        # for i, num in enumerate(nums):
        #     nums_set.remove(num)
        #     d[num] = list(nums_set)
        #     nums_set.add(num)
        
        # res = []
        
        self.backtrack([], set(nums))
        return self.res
    
    def backtrack(self, permutation: list, remaining_nums: set) -> list:
        if len(remaining_nums) == 0:
            return self.res.append(permutation.copy())

        remaining_list = list(remaining_nums)
        for num in remaining_list:
            remaining_nums.remove(num)
            permutation.append(num)
            self.backtrack(permutation, remaining_nums)
            permutation.pop()
            remaining_nums.add(num)
        
        return


        

    
    def permuteHelper(self, d):
        
        # We now have a mapping of every number in nums to all of its other numbers in nums,
        # i.e. 1:N-1 mappings! Hence, we can recursively call permute function as need be :)
        res = []
        print(f"{d=}")
        for key, arr in d.items():
            permutations = list(self.permute(arr))
            permutations.append(key)
            print(f"{key=}, {permutations=}")
            res.append(permutations.copy())
        return res