class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if all(num == k for num in nums):
            return len(nums)

        res = 0
        for duplicate_num in range(1, 51):
            # Find maximum subarray sum, where subarray sum is defined as
            # occurences of 'duplicate_num' - occurences of 'k'
            if duplicate_num == k:
                continue

            cur_sum = 0
            for num in nums:
                cur_sum += (num == duplicate_num)
                cur_sum -= (num == k)
                res = max(res, cur_sum)
                if cur_sum < 0:
                    cur_sum = 0
            res = max(res, cur_sum)

        return res + nums.count(k)


        # Problem: Find subarray sum with largest non-k duplicates
        # A subarray's "value" is the number of duplicates it has,
        # minus the number of the value k it has
        N = len(nums)
        prefix_k_count = []
        cur_count = 0
        for num in nums:
            cur_count += num == k
            prefix_k_count.append(cur_count)

        suffix_k_count = []
        cur_count = 0
        for num in reversed(nums):
            cur_count += num == k
            suffix_k_count.append(cur_count)
        suffix_k_count = suffix_k_count[::-1]

        # Sliding window. At any point if max duplicate count < k count,
        # then we want to start a NEW window
        l = 0
        k_count = 0
        d = defaultdict(int)

        res = nums.count(k)
        
        for r in range(N):
            num = nums[r]
            d[num] += 1
            k_count += num == k

            # max(d.values()) = max(d.values())
            while l < r and k_count >= max(d.values()):
                l_num = nums[l]
                k_count -= l_num == k
                d[l_num] -= 1
                assert d[l_num] >= 0
                l += 1


            if False or r - l + 1 >= 1:
                prev_res = res
                res = max(
                    res,
                    (
                        (prefix_k_count[l - 1] if l - 1 >= 0 else 0)
                        + (max(d.values()) - k_count)
                        + (suffix_k_count[r + 1] if r + 1 < N else 0)
                    )
                )
                if prev_res < res:
                    print(f"{suffix_k_count=}")
                    print(f"{l,r=}, {res=}")
                    print(f"{max(d.values()), k_count=}")
                    print(f"{prefix_k_count=}")


        r = N
        while l < r and k_count >= max(d.values()):
            l_num = nums[l]
            k_count -= l_num == k
            d[l_num] -= 1
            assert d[l_num] >= 0
            l += 1
        if False or r - l + 1 >= 2:
            res = max(
                res,
                (
                    (prefix_k_count[l - 1] if l - 1 >= 0 else 0)
                    + (max(d.values()) - k_count)
                    + (suffix_k_count[r + 1] if r + 1 < N else 0)
                )
            )

        return res
            
            
            