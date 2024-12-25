class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        letters = []
        def backtrack(i):
            if i >= len(digits):
                res.append("".join(letters))
                return
            
            # For this backtracking problem, this isn't necessarily a binary-decision
            # per every index i (which is very typical for most backtracking problems!)
            # Here instead, we want to loop through every single possible letter mapped
            # by digits[i], and then backtrack our way through for each DFS :)
            for letter in digit_to_letters[digits[i]]:
                letters.append(letter)
                backtrack(i + 1)
                letters.pop()
        
        backtrack(0)
        return res