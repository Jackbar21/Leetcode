class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        visited = set()
        double_visited = set()

        for num in nums:
            if num in double_visited:
                continue
            
            if num in visited:
                visited.remove(num)
                double_visited.add(num)
                continue
            
            assert num not in visited and num not in double_visited
            visited.add(num)
        
        assert len(visited) == 1
        return visited.pop()

