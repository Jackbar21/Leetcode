class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        N = len(nums)
        indices = []
        i = 0
        line_sweep = [0] * (N + 1)
        for i, num in enumerate(nums):
            if num == key:
                start = max(0, i - k)
                end = min(N, i + k + 1)
                line_sweep[start] += 1
                line_sweep[end] -= 1
        
        res = []
        active = 0
        for i, delta in enumerate(line_sweep):
            active += delta
            if active > 0:
                res.append(i)
        return res



        # while i < N:
        #     num = nums[i]
        #     if num != key:


        #     last_index = indices[-1] if indices else -1
        #     for index in range()

            # Loop Invariant
            # i += 1
        # for i, num in enumerate(nums):
        #     if num == key:
        #         for index in range(max(0, i - k), min(N, i + k + 1)):
        #             unique_indices.add(index)
        
        return sorted(unique_indices)
