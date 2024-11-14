class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # Essentially, we can binary search to find the smallest x
        # For any x, we can query whether it works or not. We know that
        # 1 <= x <= max(quantities), and it at some point there will be
        # some pivot i such that 1 <= x < i is not possible, but possible
        # for all i <= x <= max(quantities). We want to find this such i,
        # which we can do via leftmost binary search, where we check if a
        # certain i or x works by trying to evenly distribute each quantity
        # in batches of x (with last one being between 1 & x), and checking
        # if by doing so we need MORE than n specialty retail stores or not :)
        quantities.sort(reverse=True) # sorting, since algo O(mlogm) anyways!
        l, r = 1, quantities[0]
        # We know that since m <= n, there is always a solution at x == max(quantites)
        # since that would mean we can put each product type into a singular specialty
        # retail store, of which there are at least m many :)
        x = r
        while l <= r:
            mid = (l + r) // 2

           
            # Want to check if works
            is_valid = True

            if sum(math.ceil(quantity / mid) for quantity in quantities) <= n:
                x = mid
                # Since this is valid, we don't care about anything bigger
                # than mid! Hence, we decrease search-space to left subhalf :)
                r = mid - 1
            else:
                # mid is invalid, so any smaller value will force to ration
                # our product quantities EVEN MORE, meaning total number
                # of specialty retail stores will remain the same AT BEST,
                # and otherwise increase. Hence, if there are any solutions,
                # it will be with an x-value LARGER than mid (so search right subhalf!)
                l = mid + 1
        
        return x