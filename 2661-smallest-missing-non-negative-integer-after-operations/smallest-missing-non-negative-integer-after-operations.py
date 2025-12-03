class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num % value] += 1
        print(f"{d=}")
        for i in range(len(nums)):
            if d[i % value] == 0:
                return i
            d[i % value] -= 1
        return len(nums)