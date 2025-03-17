class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        return all(val % 2 == 0 for val in d.values())