class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N = len(nums)

        # Compute prefix maxes for all of nums!
        prefix_max = [] # prefix_max[i] == max(nums[i:])
        cur_max = float("-inf")
        for num in reversed(nums):
            if cur_max < num:
                cur_max = num
            prefix_max.append(cur_max)
        prefix_max = prefix_max[::-1]
        
        res = 0
        best_i = float("-inf")
        for j in range(1, N - 1):
            # Get largest value of nums[i], such that i < j
            prev_val = nums[j - 1]
            if best_i < prev_val:
                best_i = prev_val

            # Get largest value of nums[k], such that j < k
            best_k = prefix_max[j + 1]

            # Compute optimal val for index j
            val = (best_i - nums[j]) * best_k

            # Update res if val is larger than current best result!
            if res < val:
                res = val

        # Return best result
        return res
