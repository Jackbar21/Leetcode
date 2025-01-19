class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.s1, self.s2, self.s3 = s1, s2, s3
        self.memo = {}
        return self.dp(0, 0, 0)

    # @cache
    def dp(self, s1_index, s2_index, s3_index):
        if (s1_index, s2_index, s3_index) in self.memo:
            return self.memo[(s1_index, s2_index, s3_index)]
        
        if s3_index >= len(self.s3):
            return s1_index >= len(self.s1) and s2_index >= len(self.s2)
        
        s1_letter = None if s1_index >= len(self.s1) else self.s1[s1_index]
        s2_letter = None if s2_index >= len(self.s2) else self.s2[s2_index]
        s3_letter = self.s3[s3_index]
        
        # s1_letter, s2_letter, s3_letter = self.s1[s1_index], self.s2[s2_index], self.s3[s3_index]

        if s3_letter != s1_letter and s3_letter != s2_letter:
            return False
        
        if s3_letter == s1_letter and s3_letter != s2_letter:
            res = self.dp(s1_index + 1, s2_index, s3_index + 1)
            self.memo[(s1_index, s2_index, s3_index)] = res
            return res
        
        if s3_letter != s1_letter and s3_letter == s2_letter:
            res = self.dp(s1_index, s2_index + 1, s3_index + 1)
            self.memo[(s1_index, s2_index, s3_index)] = res
            return res
        
        res = (
            self.dp(s1_index + 1, s2_index, s3_index + 1) 
            or self.dp(s1_index, s2_index + 1, s3_index + 1)
        )
        self.memo[(s1_index, s2_index, s3_index)] = res
        return res

