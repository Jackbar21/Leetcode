class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Want to find a pair (i,j) such that 0 <= i,j < len(nums), and 
        # nums[i] + nums[j] == target
        seen = {}
        for i, num in enumerate(nums):
            # Want a wanted_num such that num + wanted_num == target
            # <--> wanted_num == target - num
            wanted_num = target - num
            if wanted_num in seen:
                return (seen[wanted_num], i)

            seen[num] = i
        
        raise Exception("Unreachable Code -- must exist at least one solution")