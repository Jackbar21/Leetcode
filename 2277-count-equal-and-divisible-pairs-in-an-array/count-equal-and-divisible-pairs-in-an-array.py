class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # One Liner Solution:
        # return sum((nums[i] == nums[j] and (i * j) % k == 0) for i in range(len(nums)) for j in range(i + 1, len(nums)))

        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                is_valid = (nums[i] == nums[j]) and (i * j) % k == 0
                if is_valid:
                    res += 1
        return res


        res = 0

        # Step 1: Map all nums to their indices
        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)
        
        # Step 2: For each num, loop through all pairs of indices and check if divisible by k
        for indices in d.values():
            for i, index_i in enumerate(indices):
                for j in range(i + 1, len(indices)):
                    res += (index_i * indices[j]) % k == 0

        return res
