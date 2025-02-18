class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # return self.naive(pattern)

        # Instead of raw brute force, we can also try backtracking!
        # Since we want lexicographically SMALLEST result, we can enumerate
        # the possible strings in order of smallest to largest lexicographically,
        # and stop as soon as we find one that is valid :)
        available_nums = set("123456789")
        res = []
        def backtrack(i):
            sorted_nums = sorted(available_nums)
            prev = res[-1] if len(res) > 0 else float("-inf")
            
            if i == len(pattern) + 1:
                return True

            for num in sorted_nums:
                if (i > 0) and (
                    (pattern[i - 1] == "I" and prev >= num) or 
                    (pattern[i - 1] == "D" and prev <= num)
                ):
                    continue
                
                res.append(num)
                available_nums.remove(num)
                if backtrack(i + 1):
                    return True
                res.pop()
                available_nums.add(num)

            return False
        
        backtrack(0)
        return "".join(res)

    





    def naive(self, pattern: str) -> str:
        for num in itertools.permutations("123456789", len(pattern) + 1):
            if self.isValid(num, pattern):
                return "".join(num)
    
    def isValid(self, num: tuple, pattern: str) -> bool:
        for i in range(len(num) - 1):
            cur_num, next_num = num[i], num[i + 1]
            if (
                (pattern[i] == "I" and cur_num >= next_num) or 
                (pattern[i] == "D" and cur_num <= next_num)
            ):
                return False

        return True