class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = pow(10, 9) + 7
        N = len(nums)

        # nums[i] == 2 * nums[j]
        # nums[k] == 2 * nums[j]
        # What this means, is for every index j, we must count how many elements
        # to the left of j have value 2 * nums[j], as well as how many on the right
        # have same value 2 * nums[j]. Then, we multiply these two values together, for each j.
        # To do this, we need to keep track of the frequencies of each num to the left and right
        # of each index j. We can keep track of these AS we loop through each index j!

        left = defaultdict(int)
        right = defaultdict(int)
        for num in nums:
            right[num] += 1
        
        res = 0
        for j, num in enumerate(nums):
            right[num] -= 1

            target = 2 * num
            res = (res + left[target] * right[target]) % MOD

            left[num] += 1

        return res % MOD
