class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)
        d = defaultdict(int)
        for i, num in enumerate(nums):
            d[num - i] += 1
        
        good_pairs = 0
        for k in d.values():
            good_pairs += (k * (k - 1)) // 2

        total_pairs = (N * (N - 1)) // 2
        bad_pairs = total_pairs - good_pairs
        return bad_pairs
        
        print(f"{d=}")
        res = 0
        N = len(nums)
        for i in range(N):
            num_i = nums[i]
            for j in range(i + 1, N):
                res += (j - i != nums[j] - num_i)
        return res
        # return sum(j - i != nums[j] - nums[i] for i in range(len(nums)) for j in range(i + 1, len(nums)))

        # Idea: Let N = len(nums). Then, there are N * (N - 1) / 2 total possible pairs. Since there are
        # likely much fewer good pairs than there are bad, given we know there are k good pairs, the number
        # of bad pairs is simply (N * (N - 1) / 2) - K.

        # A pair of indices (i, j) is a GOOD PAIR if i >= j or j - i == nums[j] - nums[i]
        # j + nums[i] != i + nums[j]
        # nums[i] - i != nums[j] - j
