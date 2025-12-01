class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # Sort
        N = len(batteries)
        batteries.sort()

        # Prefix sums
        prefix = []
        cur_sum = 0
        for battery in batteries:
            cur_sum += battery
            prefix.append(cur_sum)
        
        def getLimitedSum(limit: int) -> int:
            # Compute sum of batteries where we can only use at most
            # 'limit' per battery.
            # We can do this via leftmost binary search, by finding 
            # leftmost index l such that batteries[l] > limit (if any)
            if batteries[-1] <= limit:
                return sum_batteries
            elif batteries[0] >= limit:
                return limit * N
            
            l, r = 0, N - 1
            while l <= r:
                mid = (l + r) // 2
                if batteries[mid] > limit:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # assert l > 0
            return prefix[l - 1] + limit * (N - l)

        sum_batteries = prefix[-1]
        l, r = 0, sum_batteries
        while l <= r:
            mid = (l + r) // 2
            # Check if can have all N computers running for 'mid' time
            # If a battery is more than 'mid', only 'mid' of it can be used
            amount_needed = mid * n
            amount_have = getLimitedSum(mid)
            if amount_have >= amount_needed:
                # Look for potentially larger but also correct solutions
                l = mid + 1
            else:
                # Look for smaller but potentially correct solutions
                r = mid - 1
        
        return r
