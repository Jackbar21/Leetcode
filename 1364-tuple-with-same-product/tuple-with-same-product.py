class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        N = len(nums)
        d = defaultdict(list)

        for i, num in enumerate(nums):
            for j in range(i + 1, N):
                product = num * nums[j]
                d[product].append((i, j))
        
        # print(f"{d=}")

        # For each array in dict of length N, there will be such many pairs:
        #   1 + 2 + 3 + ... + N - 1
        #   == (1 + 2 + 3 + ... + N) - N
        #   == N(N+1)/2 - N
        #   == (N^2+N)/2 - (2N/2)
        #   == (N^2+N-2N)/2
        #   == (N^2-N)/2
        #   == N(N-1)/2
        # Now for every valid pair, we can construct 8 valid tuple permutations. So for each product,
        # we will consider the total number of tuples as the number of pairs multiplied by 8! We simply
        # take the sum of this value fore each product in d as our result :)
        res = 0
        for key in d:
            count = len(d[key])
            num_pairs = (count * (count - 1)) // 2
            res += num_pairs * 8
        return res

        # Brute Force: O(N^4) solution!
        # N = len(nums)
        # res = 0
        # for i in range(N):
        #     for j in range(i + 1, N):
        #         for k in range(j + 1, N):
        #             for l in range(k + 1, N):
        #                 a, d, c, b = sorted([nums[i], nums[j], nums[k], nums[l]])
        #                 if a != b != c != d and a * b == c * d:
        #                     res += 8
        # return res