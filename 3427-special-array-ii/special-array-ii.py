class Solution:
    def getSubarraySum(self, i, j):
        return self.prefix_sums[j] - (self.prefix_sums[i - 1] if i > 0 else 0)
    
    def isSpecial(self, i, j):
        assert i <= j
        nums = self.nums
        if i == j:
            return True
        
        expected = j - i + 1 # i.e. length!
        actual = (
            self.isDifferentParity(nums[i], nums[i + 1])   # first number
            + self.getSubarraySum(i + 1, j - 1)            # in-between numbers
            + self.isDifferentParity(nums[j - 1], nums[j]) # last number
        )
        return expected == actual
    def isDifferentParity(self, num1, num2):
        return ((num1 % 2) ^ (num2 % 2)) == 1
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        if len(nums) == 1:
            return [True] * len(queries)
        #print(nums)
        self.nums = nums
        prev = None
        is_special = {} # i: nums[i] is special!
        # Handle first elements
        is_special[0] = self.isDifferentParity(nums[0], nums[1])
        
        # Handle every number in between
        for i in range(1, len(nums) - 1):
            prev_num, num, post_num = nums[i - 1], nums[i], nums[i + 1]
            is_special[i] = self.isDifferentParity(prev_num, num) and self.isDifferentParity(num, post_num)
        
        # Handle last element
        is_special[len(nums) - 1] = self.isDifferentParity(nums[-2], nums[-1])
        # self.is_special = is_special
        #print(f"{is_special=}")
        #print(sum(is_special.values()))

        # Now, do prefix sums but based on these True/False values (as 1 and 0, respectively!)
        prefix_sums = []
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += is_special[i]
            prefix_sums.append(cur_sum)
        self.prefix_sums = prefix_sums
        #print(f"{prefix_sums=}")

        FROM, TO = 0, 1
        return [
            self.isSpecial(query[FROM], query[TO])
            for query in queries
        ]

