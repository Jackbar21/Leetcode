class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # If there are N numbers with the same value in nums[l..r], 
        # then there are N(N-1)/2 pairs of indices (i, j) such that
        # l <= i < j <= r and arr[i] == arr[j].
        N = len(nums)
        res = 0

        d = defaultdict(int)
        num_pairs = 0

        l = 0
        for r, r_num in enumerate(nums):
            num_pairs += d[r_num]
            d[r_num] += 1

            while num_pairs >= k:
                # nums[l..r] is valid, which means nums[l..r']
                # is valid for all r <= r' < N, where N == len(nums)
                # Hence, this makes for a total of N - r valid subarrays!
                res += N - r
                assert l < r
                l_num = nums[l]
                d[l_num] -= 1
                assert d[l_num] >= 0
                num_pairs -= d[l_num]
                l += 1

        return res

        
        prefix_freqs = []
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
            prefix_freqs.append(d.copy())
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                d_big = prefix_freqs[j]
                d_small = prefix_freqs[i - 1] if i - 1 >= 0 else {}
                d = {
                    key: val - d_small.get(key, 0)
                    for key, val in d_big.items()
                }
                # print(f"nums[{i}..{j}]={nums[i:j+1]}, {d=}")

                num_pairs = 0
                for num, freq in d.items():
                    # num_pairs = (val * (val - 1)) // 2
                    # res += num_pairs >= k
                    num_pairs += (freq * (freq - 1)) // 2
                res += num_pairs >= k
        
        return res