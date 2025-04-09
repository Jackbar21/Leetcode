class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # For fun, here is a one line solution!
        # return -1 if min(nums) < k else len(set(filter(lambda num: num > k, nums)))

        # We can only make numbers SMALLER. So to make every number equal to k,
        # it cannot be that ANY number is smaller than k inside of nums!
        if min(nums) < k:
            return -1
        
        # Want to find the number of UNIQUE numbers that are larger than k! Since if
        # the only unique numbers we have larger than k are X < Y < Z, then we must:
        # (1) Convert all copies of Z into Y
        # (2) Convert all copies of Y into X
        # (3) Convert all copies of X into k
        # So the number of unique numbers larger than k is the solution to this problem!
        larger_nums = set(nums)
        larger_nums.discard(k)
        return len(larger_nums)
