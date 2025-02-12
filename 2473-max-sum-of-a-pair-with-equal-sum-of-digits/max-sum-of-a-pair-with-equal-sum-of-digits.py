class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Overall idea (in steps:)
        # Step 1: Convert all the numbers to sum of digits
        # Step 2: Obtain the FREQUENCY of each sum!
        # Step 3: Grab largest sum whose frequency is GREATER THAN 1

        d = defaultdict(list)
        for num in nums:
            sum_digits = functools.reduce(lambda acc, x: acc + int(x), str(num), 0)
            d[sum_digits].append(num)
            d[sum_digits].sort(reverse=True)
            while len(d[sum_digits]) > 2:
                d[sum_digits].pop()
        
        max_val = -1
        for nums_with_same_digit_sum in d.values():
            if len(nums_with_same_digit_sum) > 1:
                max_val = max(max_val, sum(nums_with_same_digit_sum))
        return max_val