class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = pow(10, 9) + 7

        d = defaultdict(int)
        for x, y in points:
            d[y] += 1
        
        # For any two pair of points A and B with the same y intercept,
        # it can form a trapezoid with any other two pair of points A' and B'
        # with the same y' intercept, where y != y'
        #
        # The dictionary d maps the y coordinates to the number of points including that coordinate.
        #
        # We know for each y, where N = d[y], then there are N * (N + 1) / 2 possible
        # pair of points.
        #
        # It can then form a trapezoid with each of the N' * (N' + 1) / 2 possible pair of
        # points, for each d[y'] such that y != y'
        pair_counts = [(n * (n - 1)) // 2 for n in d.values()]
        remaining_pair_count = sum(pair_counts)

        res = 0
        for pair_count in pair_counts:
            remaining_pair_count -= pair_count
            res += pair_count * remaining_pair_count
            res %= MOD
        return res
