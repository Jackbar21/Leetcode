class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = "99"
        for num in map("".join, itertools.permutations("123456789", len(pattern) + 1)):
            if num < res and self.isValid(num, pattern):
                res = num
        return res
    
    def isValid(self, num: str, pattern: str) -> bool:
        assert len(num) == len(pattern) + 1
        N = len(num)

        for i in range(N - 1):
            if pattern[i] == "I" and not (num[i] < num[i + 1]):
                return False
            elif pattern[i] == "D" and not (num[i] > num[i + 1]):
                return False

        return True