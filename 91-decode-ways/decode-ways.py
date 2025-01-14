class Solution:
    def numDecodings(self, s: str) -> int:
        self.s, self.memo = s, {}
        return self.dp(0)
    
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]
        s = self.s
        
        # After end of string, found a valid combination!
        if i >= len(s):
            return 1
        
        digit = int(s[i])
        
        # Trailing 0, must be INVALID encoding!
        if digit == 0:
            # Return 0, since NO MORE POSSIBILTIES from this point onwards!
            return 0

        if digit != 1 and digit != 2:
            # Only one possible case: consider digit as single digit only!
            res = self.dp(i + 1)
            self.memo[i] = res
            return res

        if digit == 1:
            # Case 1: Only consider single digit here, can only do so if next digit
            # is NOT a zero (as otherwise it would be trailing!)
            case1 = 0
            if not (i + 1 < len(s) and s[i + 1] == "0"):
                case1 = self.dp(i + 1)

            # Case 2: Consider two digit number!
            case2 = 0
            if i + 1 < len(s):
                case2 = self.dp(i + 2)

            res = case1 + case2
            self.memo[i] = res
            return res
        
        # assert digit == 2
        # Case 1: Only consider single digit here, can only do so if next digit
        # is NOT a zero (as otherwise it would be trailing!)
        case1 = 0
        if not (i + 1 < len(self.s) and self.s[i + 1] == "0"):
            case1 = self.dp(i + 1)

        # Case 2: Consider two digit number! Can only do so if second if second digit is
        # between 0 and 6 (since 27, 28, 29 are invalid encodings!)
        case2 = 0
        if i + 1 < len(self.s) and 0 <= int(self.s[i + 1]) <= 6:
            case2 = self.dp(i + 2)

        res = case1 + case2
        self.memo[i] = res
        return res
