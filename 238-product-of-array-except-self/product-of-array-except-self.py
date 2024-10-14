class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # answer[i] = prefix_mults[i-1] * suffix_mults[i+1]
        # answer[i + 1] = prefix_mults[i] * suffix_mults[i+2]

        # Idea (Constant Space):
        #   prefix = nums[0], i = 0
        #   suffix = nums[-1], i = len(nums) - 1
        # Start off with answer = [1,1,1,1,1,...,1]
        # We know that we want to multiply answer[i] with prefix_mults[i - 1]
        # as well as suffix_mults[i + 1]. So as we build up our prefix value,
        # start with prefix = nums[0], multiplying it by nums[1], then nums[2],
        # so on and so on (and similarly for suffix in a secondary O(n) sweep),
        # We can multiply the current value of prefix where after i iterations,
        # prefix = nums[0] * ... * nums[i] to answer[i+1], and then after i
        # iterations, suffix = nums[len(nums) - 1] * ... * nums[i] to answer[i - 1].

        # Step 1: Initialize answer array
        answer = [1] * len(nums)

        # Step 2: Prefix multiplications
        i = 0
        prefix = nums[i]
        while i + 1 < len(nums):
            answer[i + 1] *= prefix

            # Loop Invariant
            i += 1
            prefix *= nums[i]
        
        # Step 3: Suffix multiplications
        i = len(nums) - 1
        suffix = nums[i]
        while i - 1 >= 0:
            answer[i - 1] *= suffix

            # Loop Invariant
            i -= 1
            suffix *= nums[i]
        
        return answer


        # Idea (Linear Space):
        # prefix_mults[i] = nums[0] * nums[1] * ... * nums[i]
        # suffix_mults[i] = nums[i] * nums[i+1] * ... * nums[len(nums) - 1]
        # answer[i] = prefix_mults[i-1] * suffix_mults[i+1]

        # Step 1: build prefix_mults
        base = 1
        prefix_mults = []
        for num in nums:
            base *= num
            prefix_mults.append(base)
        
        # Step 2: build suffix_mults
        base = 1
        suffix_mults = collections.deque([])
        for i in range(len(nums) - 1, -1, -1):
            base *= nums[i]
            suffix_mults.appendleft(base)

        # Step 3: build answer
        answer = [suffix_mults[1]]
        for i in range(1, len(nums) - 1):
            answer.append(prefix_mults[i - 1] * suffix_mults[i + 1])
        answer.append(prefix_mults[-2])
        return answer