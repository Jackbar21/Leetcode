class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # If there are N numbers with the same value in nums[l..r], 
        # then there are N(N-1)/2 pairs of indices (i, j) such that
        # l <= i < j <= r and arr[i] == arr[j].
        N = len(nums)
        res, l, num_pairs = 0, 0, 0
        d = {}
        for r, r_num in enumerate(nums):
            cur_freq = d.get(r_num, 0)
            d[r_num] = cur_freq + 1
            num_pairs += cur_freq

            while num_pairs >= k:
                # nums[l..r] is valid, which means nums[l..r']
                # is valid for all r <= r' < N, where N == len(nums)
                # Hence, this makes for a total of N - r valid subarrays!
                res += N - r
                # assert l < r
                l_num = nums[l]
                new_freq = d[l_num] - 1
                d[l_num] = new_freq
                # assert d[l_num] >= 0
                num_pairs -= new_freq
                l += 1

        return res
