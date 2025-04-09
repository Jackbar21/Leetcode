class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # if min(nums) < k:
        #     return -1
        
        # Want to find the number of UNIQUE numbers that are larger than k! Since if
        # the only unique numbers we have larger than k are X < Y < Z, then we must:
        # (1) Convert Z into Y
        # (2) Convert Y into X
        # (3) Convert X into k
        # So the number of unique numbers larger than k is the solution to this problem!
        larger_nums = set()
        for num in nums:
            if num < k:
                return -1
            if num > k:
                larger_nums.add(num)
        return len(larger_nums)
