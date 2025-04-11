class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        return sum((len(str(num)) % 2 == 0 and sum(int(str(num)[i]) for i in range(len(str(num)) // 2)) == sum(int(str(num)[i]) for i in range(len(str(num)) // 2, len(str(num))))) for num in range(low, high + 1))