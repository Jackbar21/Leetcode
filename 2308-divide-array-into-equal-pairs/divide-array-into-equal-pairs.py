class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        return all(freq % 2 == 0 for freq in d.values())