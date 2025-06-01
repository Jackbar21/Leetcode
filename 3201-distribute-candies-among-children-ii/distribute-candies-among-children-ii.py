class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Notice that when we pick number of candies for first and second child, call these c1 & c2
        # respectively, the third is left with n - c1 - c2 candies, where it must be that
        # n - c1 - c2 >= 0.
        # First child gets 0 <= c1 <= min(limit, n) candies.
        # Second child gets 0 <= c2 <= min(limit, n - c1) candies.
        # Third child gets n - c1 - c2 candies [Fixed!]

        # Thus, for each amount of candy the first child can get,
        # we can compute that there are min(limit, n - c1) - 0 + 1 total
        # number of candies the second child can get.
        # However, it must be that the third child gets all the remaining
        # candy, where the third child can only consume up to limit number
        # of candies! So we must limit ourselves to limit
        res = 0
        for c1 in range(min(limit, n) - 0 + 1):
            # First child consumed c1 candy.
            # Second child can consume up to min(limit, n - c1) amount of candy,
            # call it c2.
            # Then, third child has to consume remaining n - c1 - c2 candy, but is
            # limited by limit!
            # Therefore, assuming second child eats 'limit' candy, third child has
            # to consume n - c1 - limit candy (which is best case scenario, i.e.
            # the smallest number it could have to eat and therefore most likely
            # case to be ABLE to eat)

            # Hence, it really depends how many candies the second child can choose
            # not to consume, but still have third child be able to consume ALL
            # remaining candy! So third child can consume only up to theoretical
            # MAXIMUM of min(limit, n - c1 - 0) candies (when second child eats no candy), 
            # but at MINIMUM n - c1 - limit (when second child eats limit candy)

            # Hence, if the first child consumes c1 candy, then the range of candies for
            # third child is simply [max(0, n - c1 - limit), min(limit, n - c1 - 0)]
            res += max(0, (min(limit, n - c1 - 0)) - (max(0, n - c1 - limit)) + 1)
        return res
