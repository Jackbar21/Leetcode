class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Idea:
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