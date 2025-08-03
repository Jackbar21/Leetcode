class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # This problem seems rather simple. If choose to go x steps to the right, then it
        # takes x steps to get back to start pos, meaning I can only traverse up to
        # k - 2x steps on the left (or 0, if negative). Thus we can enumerate over all possible
        # cases, i.e. 1 step to the right, 2 steps to the right, ..., k steps to the right,
        # and for each compute fruits gotten from taking max(0, k - 2x) steps to the left.
        # To make these lookups in constant time, we use prefix sums for left and right positions.
        res = 0

        left_sums = [0] * (k + 1)
        right_sums = [0] * (k + 1)

        for position, amount in fruits:
            if position <= startPos:
                # Can only reach position if at most k steps away from start pos
                distance = (startPos - position)
                if distance <= k:
                    left_sums[distance] += amount
            else:
                # Deliberately don't include zero steps away case, so doesn't
                # get double counted!
                distance = (position - startPos)
                if distance <= k:
                    right_sums[distance] += amount
        
        left_prefix_sums, right_prefix_sums = [], []

        cur_sum = 0
        for amount in left_sums:
            cur_sum += amount
            left_prefix_sums.append(cur_sum)

        cur_sum = 0
        for amount in right_sums:
            cur_sum += amount
            right_prefix_sums.append(cur_sum)
        
        res = 0
        for x in range(k + 1):
            # Case 1: Take x steps to the right, then circle back to take as many steps left
            case1 = 0

            # We take x steps to the right
            case1 += right_prefix_sums[x]

            # We take max(0, k - 2x) steps to the left
            case1 += left_prefix_sums[max(0, k - x - x)]

            # Case 2: We take as many steps x' left as possible, such that we can still
            # take x' + x steps to the right. So we need x' + x' + x <= k, LEQ to
            # x' <= (k - x) / 2, which we can binary search for!
            l = 0
            r = max(0, math.ceil((k - x) / 2))
            x_prime = -1
            while l <= r:
                mid = (l + r) // 2
                is_valid = mid <= (k - x) / 2
                if is_valid:
                    # Great, look for potentially bigger valid solutions!
                    assert x_prime < mid
                    x_prime = mid
                    l = mid + 1
                else:
                    # Invalid, look for smaller but valid solutions
                    r = mid - 1
            
            assert x_prime <= (k - x) / 2
            assert not (x_prime + 1 <= (k - x) / 2)
            case2 = left_prefix_sums[x_prime] + right_prefix_sums[x]

            profit = max(case1, case2)
            if res < profit:
                res = profit
        return res
