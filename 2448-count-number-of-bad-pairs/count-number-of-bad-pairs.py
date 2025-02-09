class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # Idea: Let N = len(nums). Then, there are N * (N - 1) / 2 total possible pairs. Since there are
        # likely much fewer good pairs than there are bad, given we know there are k good pairs, the number
        # of bad pairs is simply (N * (N - 1) / 2) - K.
        # A pair of indices (i, j) is a GOOD PAIR if i >= j or j - i == nums[j] - nums[i]
        # <==> j + nums[i] != i + nums[j]
        # <==> nums[i] - i != nums[j] - j
        # Hence for every single index i, we can map it to the value nums[i] - i, to use it for
        # comparison with other indices in nums! Then if two indices map to the same value, we know
        # those indices form ONE GOOD PAIR! Hence, we can add the frequency of each of these "values"
        # to a hash map, then counting number of total good pairs, subtracting that from the total
        # number of pairs in general, to finally obtain the number of BAD pairs.
        N = len(nums)
        d = defaultdict(int)
        for i, num in enumerate(nums):
            d[num - i] += 1

        good_pairs = functools.reduce(lambda acc, k: acc + k * (k - 1) // 2, d.values(), 0)
        total_pairs = N * (N - 1) // 2
        bad_pairs = total_pairs - good_pairs
        return bad_pairs