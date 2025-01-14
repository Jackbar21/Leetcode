class Solution:
    def numDecodings(self, s: str) -> int:
        self.s, self.memo = s, {}
        self.is_valid_encoding = True
        res = self.dp(0)
        return self.dp(0) if s[0] != 0 else 0
    
    # @cache
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]
        
        # if not self.is_valid_encoding:
        #     return 0
        
        # After end of string, found a valid combination!
        if i >= len(self.s):
            return 1
        
        digit = int(self.s[i])
        
        # Trailing 0, must be INVALID encoding!
        if digit == 0:
            self.is_valid_encoding = False
            return 0


        if digit != 1 and digit != 2:
            # 
            self.memo[i] = self.dp(i + 1)
            return self.memo[i]
            # return 1 + self.dp(i + 1)
        
        if digit == 1:
            # Case 1: Only consider single digit here, can only do so if next digit
            # is NOT a zero (as otherwise it would be trailing!)
            case1 = 0
            if not (i + 1 < len(self.s) and self.s[i + 1] == "0"):
                case1 = self.dp(i + 1)
            print(f"{digit=}, {case1=}")
            
            # Case 2: Consider two digit number!
            case2 = 0
            if i + 1 < len(self.s):
                case2 = self.dp(i + 2)
            print(f"{digit=}, {case2=}")

            self.memo[i] = case1 + case2
            return self.memo[i]
        
        assert digit == 2
        # Case 1: Only consider single digit here, can only do so if next digit
        # is NOT a zero (as otherwise it would be trailing!)
        case1 = 0
        if not (i + 1 < len(self.s) and self.s[i + 1] == "0"):
            case1 = self.dp(i + 1)
        print(f"{digit=}, {case1=}")
        
        # Case 2: Consider two digit number! Can only do so if second if second digit is
        # between 0 and 6 (since 27, 28, 29 are invalid encodings!)
        case2 = 0
        if i + 1 < len(self.s) and 0 <= int(self.s[i + 1]) <= 6:
            case2 = self.dp(i + 2)
        print(f"{digit=}, {case2=}")

        self.memo[i] = case1 + case2
        return self.memo[i]