class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = pow(10, 9) + 7

        d = defaultdict(int)
        for x, y in points:
            d[y] += 1
        print(f"{d=}")

        if len(d) <= 1:
            return 0
        
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

        # pair_counts = list(map(lambda n: (n * (n - 1)) // 2, d.values()))
        pair_counts = []
        for n in d.values():
            if n < 2:
                continue
            # if n > 1:
            #     pair_counts.append(n * (n - 1) // 2)
            count = (n * (n - 1)) // 2
            pair_counts.append(count)
        total_pairs = sum(pair_counts)
        print(f"{pair_counts=}")

        # res = functools.reduce(lambda x, y: (x * y) % MOD, pair_counts, 1)
        # # return res if res > 1 else 0
        # print(f"{pair_counts=}")
        # if len(pair_counts) <= 1:
        #     return 0
        # return min(res, total_pairs)
        suffix_sums = collections.deque([])
        cur_sum = 0
        for count in pair_counts[::-1]:
            cur_sum += count
            suffix_sums.appendleft(cur_sum)
        suffix_sums = list(suffix_sums)
        suffix_sums.append(0)

        res = 0
        for i, pair_count in enumerate(pair_counts):
            # other_pairs = total_pairs - pair_count
            other_pairs = suffix_sums[i + 1]
            res += pair_count * other_pairs
            res %= MOD
        return res
