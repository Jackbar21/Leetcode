class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Firstly, a triangle cannot be formed if the length
        # of the longest side is LARGER than (or equal to) 
        # the sum of the lengths of the other two sides!
        nums.sort()
        assert len(nums) == 3
        if nums[-1] >= nums[0] + nums[1]:
            return "none"

        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        equal_sides_count = max(d.values())

        assert 1 <= equal_sides_count <= 3
        return (
            "equilateral" if equal_sides_count == 3
            else "isosceles" if equal_sides_count == 2
            else "scalene"
        )