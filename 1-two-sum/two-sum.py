class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Want two nums num1 and num2 such that:
        #   num1 + num2 = target
        # For each num, if we keep track of nums we've seen, we
        # can check if we've already found a number whose value
        # is target - num, since of course:
        #   num + (target - num) = target

        seen = {} # num-to-index mappings
        for index, num in enumerate(nums):
            wanted_num = target - num

            if wanted_num in seen:
                prev_index = seen[wanted_num]
                return (prev_index, index)
            
            # Don't have desired num, so add current one to "seen"
            seen[num] = index
        
        raise Exception("Error: Should not reach here.")