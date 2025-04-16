class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # If there are N numbers with the same value in nums[l..r], 
        # then there are N(N-1)/2 pairs of indices (i, j) such that
        # l <= i < j <= r and arr[i] == arr[j].
        N = len(nums)
        res, l, num_pairs = 0, 0, 0
        d = defaultdict(int)
        for r, r_num in enumerate(nums):
            num_pairs += d[r_num]
            d[r_num] += 1

            while num_pairs >= k:
                # nums[l..r] is valid, which means nums[l..r']
                # is valid for all r <= r' < N, where N == len(nums)
                # Hence, this makes for a total of N - r valid subarrays!
                res += N - r
                # assert l < r
                l_num = nums[l]
                d[l_num] -= 1
                # assert d[l_num] >= 0
                num_pairs -= d[l_num]
                l += 1

        return res
