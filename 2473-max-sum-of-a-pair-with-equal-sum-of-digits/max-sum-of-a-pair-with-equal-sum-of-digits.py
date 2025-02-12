class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Overall idea (in steps:)
        # Step 1: Convert all the numbers to sum of digits
        # Step 2: Obtain the FREQUENCY of each sum!
        # Step 3: Grab largest sum whose frequency is GREATER THAN 1

        d = defaultdict(list)
        for num in nums:
            sum_digits = functools.reduce(lambda acc, x: acc + int(x), str(num), 0)
            lst = d[sum_digits]
            lst.append(num)
            if len(lst) > 2:
                assert len(lst) == 3
                lst.sort(reverse=True)
                lst.pop()

        max_val = -1
        for nums_with_same_digit_sum in d.values():
            if len(nums_with_same_digit_sum) > 1:
                max_val = max(max_val, sum(nums_with_same_digit_sum))
        return max_val