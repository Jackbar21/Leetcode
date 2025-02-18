class Solution:
    def smallestNumber(self, pattern: str) -> str:
        for num in itertools.permutations("123456789", len(pattern) + 1):
            if self.isValid(num, pattern):
                return "".join(num)
    
    def isValid(self, num: tuple, pattern: str) -> bool:
        # assert len(num) == len(pattern) + 1
        for i in range(len(num) - 1):
            cur_num, next_num = num[i], num[i + 1]
            if pattern[i] == "I" and not (cur_num < next_num):
                return False
            elif pattern[i] == "D" and not (cur_num > next_num):
                return False
        return True