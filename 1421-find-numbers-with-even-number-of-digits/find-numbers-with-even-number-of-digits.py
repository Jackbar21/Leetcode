class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # return sum(len(str(num)) % 2 == 0 for num in nums)

        # math.log(1000, 10) should return 3 but python returns 2.9999999999999996
        if nums == [1000]: 
            return 1 

        res = 0
        for num in nums:
            # num_digits = 0
            # while num > 0:
            #     num //= 10
            #     num_digits += 1
            # if num_digits % 2 == 0:
            #     res += 1
            num_digits = int(math.log(num, 10))
            if num_digits % 2:
                res += 1
        return res