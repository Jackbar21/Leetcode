class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Overall idea (in steps:)
        # Step 1: Convert all the numbers to sum of digits
        # Step 2: Obtain the FREQUENCY of each sum!
        # Step 3: Grab largest sum whose frequency is GREATER THAN 1
        def convertNumToSumDigits(num):
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            return res

        d = defaultdict(list)
        for num in nums:
            # sum_digits = functools.reduce(lambda acc, x: acc + int(x), str(num), 0)
            sum_digits = convertNumToSumDigits(num)
            min_heap = d[sum_digits]
            heapq.heappush(min_heap, num)
            while len(min_heap) > 2:
                heapq.heappop(min_heap)
            # if len(lst) <= 2:
            #     continue
            # else:
            #     # Get rid of smallest between three numbers!
            #     # assert len(lst) == 3
            #     lst.sort(reverse=True) # O(1)
            #     lst.pop()

        max_val = -1 # default value if no results!
        for nums_with_same_digit_sum in d.values():
            if len(nums_with_same_digit_sum) > 1:
                # assert len(nums_with_same_digit_sum) == 2
                sum_nums = nums_with_same_digit_sum[0] + nums_with_same_digit_sum[1]
                if max_val < sum_nums:
                    max_val = sum_nums
        return max_val