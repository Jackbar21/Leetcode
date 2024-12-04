class Solution:
    def getNextLetter(self, letter):
        return self.d[letter]
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        d = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(alphabet) - 1):
            letter = alphabet[i]
            d[letter] = alphabet[i + 1]
        d['z'] = 'a'
        self.d = d

        self.str1, self.str2 = str1, str2

        self.is_subsequence = False
        self.memo = {}
        self.dp(0, 0)
        return self.is_subsequence
    
    @cache
    def dp(self, str1_index, str2_index):
        # At any point if we've found a valid solution, terminate all dp calls!
        if self.is_subsequence:
            return True
        
        diff1 = len(self.str1) - str1_index
        diff2 = len(self.str2) - str2_index
        if diff1 < diff2:
            return False

        # if (str1_index, str2_index) in self.memo:
        #     return self.memo[(str1_index, str2_index)]

        if str2_index >= len(self.str2):
            self.is_subsequence = True
            return True
        
        if str1_index >= len(self.str1):
            # self.memo[(str1_index, str2_index)] = False
            return False

        

        # Case 2: Include character (only do this if ACTUALLY possible!)
        case2 = False
        letter = self.str1[str1_index]
        if self.str2[str2_index] in [letter, self.d[letter]]:
            if self.dp(str1_index + 1, str2_index + 1):
                self.is_subsequence = True
                return True
        
        # Case 1: Don't include character
        case1 = self.dp(str1_index + 1, str2_index)
        if case1:
            self.is_subsequence = True
            return True

        
        res = case1 or case2
        return res
