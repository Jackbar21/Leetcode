class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N = len(nums)

        # Compute prefix maxes for all indices in nums!
        prefix_max = [] # prefix_max[i] == max(nums[i..N-1]) == max(nums[i:])
        cur_max = float("-inf")
        for num in reversed(nums):
            if cur_max < num:
                cur_max = num
            prefix_max.append(cur_max)
        prefix_max = prefix_max[::-1]

        # Compute suffix maxes for all indices in nums!
        suffix_max = [] # suffix_max[i] == max(nums[0..i]) == max(nums[:i+1])
        cur_max = float("-inf")
        for num in nums:
            if cur_max < num:
                cur_max = num
            suffix_max.append(cur_max)
        
        res = 0
        for j in range(1, N - 1):
            # Get largest value of nums[i], such that i < j
            best_i = suffix_max[j - 1]

            # Get largest value of nums[k], such that j < k
            best_k = prefix_max[j + 1]

            # Compute optimal val for index j
            val = (best_i - nums[j]) * best_k

            # Update res if val is larger than current best result!
            if res < val:
                res = val

        # Return best result
        return res
