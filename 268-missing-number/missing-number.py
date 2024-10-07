class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        visited = set(range(len(nums) + 1))
        for num in nums:
            assert num in visited
            visited.remove(num)
        
        assert len(visited) == 1
        return visited.pop()