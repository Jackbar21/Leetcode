class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        prefix_sums = []
        cur_sum = 0
        for num in nums:
            cur_sum += num
            prefix_sums.append(cur_sum)
        
        getSubarraySum = lambda i, j: prefix_sums[j] - (prefix_sums[i - 1] if i - 1 >= 0 else 0)
        getScore = lambda i, j: (j - i + 1) * getSubarraySum(i, j)

        # res = 0
        # for i in range(N):
        #     for j in range(i, N):
        #         score = getScore(i, j)
        #         # print(f"getScore({i}, {j})={score}")
        #         res += score < k
        # return res

        # Realization: Nums only consists of POSITIVE integers. So, as soon as we get to a sum
        # that's too large, we know we must stop. The number of subarrays whose score is strictly
        # less than k, is simply the total number of possible subarrays MINUS the amount of subarrays
        # whose score is >= k! Computing the latter is much simpler, as we can use sliding window trick
        # to get the job done (i.e. once nums[l..r] is valid, since all nums are positive, then
        # nums[l..r'] is also valid for all r <= r' < N).

        # Step 1: Compute total number of possible subarrays
        total_subarrays = (N * (N + 1)) // 2

        # Step 2: Count all subarrays whose score is >= k (in variable 'res')
        l = 0
        invalid_subarrays = 0
        for r, num in enumerate(nums):
            # We can compute score in O(1) time using getScore function, so don't even need to
            # keep track of a local aggregate variable as we iterate through sliding window :)
            if getScore(l, r) < k:
                continue
            
            while getScore(l, r) >= k:
                invalid_subarrays += N - r
                l += 1
        
        # Step 3: Compute valid result using computed values from steps 1 & 2
        valid_subarrays = total_subarrays - invalid_subarrays
        return valid_subarrays
