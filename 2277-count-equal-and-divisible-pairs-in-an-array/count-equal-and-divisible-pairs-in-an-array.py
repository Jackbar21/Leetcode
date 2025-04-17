class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # return sum((nums[i] == nums[j] and (i * j) % k == 0) for i in range(len(nums)) for j in range(i + 1, len(nums)))

        # N = len(nums)
        # res = 0
        # for i, num in enumerate(nums):
        #     for j in range(i + 1, N):
        #         res += num == nums[j] and (i * j) % k == 0
        # return res

        res = 0

        # Step 1: Map all nums to their indices
        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)
        
        # Step 2: For each num, loop through all pairs of indices and check if divisible by k
        for indices in d.values():
            for i, index_i in enumerate(indices):
                for j in range(i + 1, len(indices)):
                    index_j = indices[j]
                    res += (index_i * index_j) % k == 0
        
        return res
