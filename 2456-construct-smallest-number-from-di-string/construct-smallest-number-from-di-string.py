class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # Instead of raw brute force, we can also try backtracking!
        # Since we want lexicographically SMALLEST result, we can enumerate
        # the possible strings in order of smallest to largest lexicographically,
        # and stop as soon as we find one that is valid :)
        available_nums = set("123456789")
        res = []
        def backtrack(i):
            if i == len(pattern) + 1:
                return True

            sorted_nums = sorted(available_nums)
            prev = res[-1] if len(res) > 0 else float("-inf")
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
