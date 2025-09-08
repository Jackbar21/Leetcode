class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for num in range(1, n + 1):
            remaining = n - num
            if "0" not in str(num) and "0" not in str(remaining):
                return [num, remaining]
        return [-1, -1]