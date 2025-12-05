class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        prefix_sums = [] # prefix_sums[i] == sum(nums[0..i])
        suffix_sums = [] # suffix_sums[i] == sum(nums[i..])
        N = len(nums)
        cur_prefix_sum = 0
        cur_suffix_sum = 0
        for i in range(N):
            cur_prefix_sum += nums[i]
            cur_suffix_sum += nums[N - 1 - i]
            prefix_sums.append(cur_prefix_sum)
            suffix_sums.append(cur_suffix_sum)
        suffix_sums = suffix_sums[::-1]

        res = 0
        for i in range(N - 1):
            left_sum = prefix_sums[i]
            right_sum = suffix_sums[i + 1]
            if (left_sum - right_sum) % 2 == 0:
                res += 1
        return res