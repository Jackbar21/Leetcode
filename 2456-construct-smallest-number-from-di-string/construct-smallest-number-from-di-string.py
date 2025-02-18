class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def isValid(num: tuple, pattern: str) -> bool:
            for i in range(len(num) - 1):
                cur_num, next_num = num[i], num[i + 1]
                if (
                    (pattern[i] == "I" and cur_num >= next_num) or 
                    (pattern[i] == "D" and cur_num <= next_num)
                ):
                    return False
            return True
        for num in itertools.permutations("123456789", len(pattern) + 1):
            if isValid(num, pattern):
                return "".join(num)
    
    