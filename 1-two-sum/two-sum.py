class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            # prev_num + num == target <--> prev_num == target - num
            prev_num = target - num
            if prev_num in d:
                return (d[prev_num], i)
            d[num] = i
        raise Exception("No Solution")
