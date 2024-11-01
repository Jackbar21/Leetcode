class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        completed = set()

        # Now that nums is sorted, idea is to 
        for i in range(len(nums)):
            if nums[i] in completed:
                continue

            case_i = self.twoSumIISolver(nums, i)
            res.extend(case_i)
            completed.add(nums[i])
        
        return res

    def twoSumIISolver(self, nums, i):
        num_i = nums[i]
        target = -num_i
        res = set()

        l, r = i + 1, len(nums) - 1
        while l < r:
            num_j, num_k = nums[l], nums[r]

            if num_j + num_k == target:
                # Here we're not able to return immediately. 
                # Consider a case such as:
                # [-2,0,1,1,2], where i == 0, l == 1, r == 4 (last index). This is
                # a valid solution, but if we increment & decrement both l & r, respectively,
                # we see there is another solution. So we update BOTH pointer values, searching
                # for MORE solutions if any left exist...
                res.add((num_i, num_j, num_k))
                l += 1
                r -= 1

            elif num_j + num_k < target:
                # Value is too small, so increment left pointer
                l += 1

            else:
                # assert num_j + num_k > target
                # Value is too big, so increment right pointer
                r -= 1
        
        return list(res)
            
    
    def twoSumSolver(self, nums, start_index, target):
        seen = {} # num to index mappings
        res = []

        # for i, num in enumerate(nums):
        for i in range(start_index, len(nums)):
            num = nums[i]
            # want num + other_num == target, which implies
            # other_num == target - num
            other_num = target - num
            if other_num in seen:
                res.append((seen[other_num], i))
            seen[num] = i
        
        return res