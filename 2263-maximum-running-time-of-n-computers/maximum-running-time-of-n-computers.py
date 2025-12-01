class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l, r = 0, sum(batteries)
        while l <= r:
            mid = (l + r) // 2
            # Check if can have all N computers running for 'mid' time
            # If a battery is more than 'mid', only 'mid' of it can be used
            amount_needed = mid * n
            amount_have = 0
            for battery in batteries:
                amount_have += battery if battery <= mid else mid

            if amount_have >= amount_needed:
                # Look for potentially larger but also correct solutions
                l = mid + 1
            else:
                # Look for smaller but potentially correct solutions
                r = mid - 1
        
        return r