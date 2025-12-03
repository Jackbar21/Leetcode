class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num % value] += 1
        for i in range(len(nums)):
            val = i % value
            if d[val] == 0:
                return i
            d[val] -= 1
        return len(nums)