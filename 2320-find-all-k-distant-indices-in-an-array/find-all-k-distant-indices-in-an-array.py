class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        unique_indices = set()
        for i in range(len(nums)):
            if nums[i] == key:
                for index in range(max(0, i - k), min(len(nums), i + k + 1)):
                    unique_indices.add(index)
        return sorted(unique_indices)


        N = len(nums)
        line_sweep = [0] * (N + 1)
        for i, num in enumerate(nums):
            if num == key:
                start = i - k
                end = i + k + 1
                line_sweep[start if start >= 0 else 0] += 1
                line_sweep[end if end <= N else N] -= 1
        
        res = []
        active = 0
        for i, delta in enumerate(line_sweep):
            active += delta
            if active > 0:
                res.append(i)
        return res
