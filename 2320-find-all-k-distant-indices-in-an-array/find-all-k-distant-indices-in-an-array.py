class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        N = len(nums)
        unique_indices = set()
        for i, num in enumerate(nums):
            if num == key:
                for index in range(max(0, i - k), min(N, i + k + 1)):
                    unique_indices.add(index)
        
        return sorted(unique_indices)
