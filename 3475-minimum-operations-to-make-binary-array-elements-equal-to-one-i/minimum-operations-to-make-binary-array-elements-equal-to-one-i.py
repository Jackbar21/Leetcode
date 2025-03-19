class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Algorithm: Whenever we see zero, perform a flip operation!
        # If we see a zero in last two elements of array, we return -1
        res = 0
        for i, bit in enumerate(nums):
            if bit == 0:
                if i >= len(nums) - 2:
                    return -1
                
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                res += 1
                continue
        
        return res


        # Trial one
        num_zeroes = 0
        cost = 0
        res = 0
        print(f"Count 0: {sum(num == 0 for num in nums)}")
        print(f"Count 1: {sum(num == 1 for num in nums)}")
        for num in nums:
            if num == 0:
                if num_zeroes == 0:
                    cost = 0
                num_zeroes += 1
                if num_zeroes == 3:
                    num_zeroes = 0
                    res += max(cost, 1)
                    cost = 0
                continue
            
            assert num == 1
            cost += 1
        
        print(f"{num_zeroes=}, {res=}, {cost=}")
        return res if num_zeroes == 0 else -1
        return res if cost == 0 else -1

