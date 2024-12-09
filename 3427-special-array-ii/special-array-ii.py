class Solution:
    def getSubarraySum(self, i, j):
        return self.prefix_sums[j] - (self.prefix_sums[i - 1] if i > 0 else 0)
    
    def isSpecial(self, i, j):
        if i == j:
            return True

        expected = j - i + 1 # i.e. length!
        actual = (
            self.isDifferentParity(self.nums[i], self.nums[i + 1])   # first number
            + self.getSubarraySum(i + 1, j - 1)                      # in-between numbers
            + self.isDifferentParity(self.nums[j - 1], self.nums[j]) # last number
        )
        return expected == actual

    def isDifferentParity(self, num1, num2):
        return (num1 % 2) != (num2 % 2)

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        if len(nums) == 1:
            return [True] * len(queries)
        self.nums = nums
        
        # Handle first element
        is_special = []
        is_special.append(self.isDifferentParity(nums[0], nums[1]))

        # Handle every number in between
        for i in range(1, len(nums) - 1):
            prev_num, num, post_num = nums[i - 1], nums[i], nums[i + 1]
            is_special.append(
                self.isDifferentParity(prev_num, num) 
                and self.isDifferentParity(num, post_num)
            )

        # Handle last element
        is_special.append(self.isDifferentParity(nums[-2], nums[-1]))

        # Now, do prefix sums but based on these True/False values (as 1 and 0, respectively!)
        # O(n)
        prefix_sums = [] 
        cur_sum = 0
        for boolean in is_special:
            cur_sum += boolean
            prefix_sums.append(cur_sum)
        self.prefix_sums = prefix_sums

        FROM, TO = 0, 1
        answer = [
            self.isSpecial(query[FROM], query[TO]) # O(1)
            for query in queries
        ]
        return answer
