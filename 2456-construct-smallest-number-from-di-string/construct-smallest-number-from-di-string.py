class Solution:
    def smallestNumber(self, pattern: str) -> str:
        for num in itertools.permutations("123456789", len(pattern) + 1):
            if self.isValid(num, pattern):
                return "".join(num)
    
    def isValid(self, num: tuple, pattern: str) -> bool:
        assert len(num) == len(pattern) + 1
        N = len(num)

        for i in range(N - 1):
            if pattern[i] == "I" and not (num[i] < num[i + 1]):
                return False
            elif pattern[i] == "D" and not (num[i] > num[i + 1]):
                return False

        return True