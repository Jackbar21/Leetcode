class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.s1, self.s2, self.s3 = s1, s2, s3
        self.memo = {}
        # return self.dp3D(0, 0, 0)

        # Bottom Up Approach (2D DP... done so by realizing
        # that only two 2D-space arrays needed at a time!)
        S1, S2, S3 = len(s1), len(s2), len(s3)
        dp = [[[False] * (S3 + 1) for _ in range((S2 + 1))] for _ in range((S1 + 1))]
        dp[S1][S2][S3] = True
        # dp = [[False] * (S2 + 1) for _ in range(S1 + 1)]
        # dp[S1][S2] = True
        for s3_index in range(S3 - 1, -1, -1):
            dp_new = [[False] * (S2 + 1) for _ in range(S1 + 1)]
            s3_letter = s3[s3_index]

            for s2_index in range(S2, -1, -1):
                s2_letter = None if s2_index >= len(self.s2) else self.s2[s2_index]
                
                for s1_index in range(S1, -1, -1):
                    s1_letter = None if s1_index >= len(self.s1) else self.s1[s1_index]
                
                    if s3_letter != s1_letter and s3_letter != s2_letter:
                        continue # Keep as False!
                    
                    if s3_letter != s2_letter:
                        dp[s1_index][s2_index][s3_index] = dp[s1_index + 1][s2_index][s3_index + 1]
                        # dp_new[s1_index][s2_index] = dp[s1_index + 1][s2_index]
                        continue
    
                    if s3_letter != s1_letter:
                        dp[s1_index][s2_index][s3_index] = dp[s1_index][s2_index + 1][s3_index + 1]
                        # dp_new[s1_index][s2_index] = dp[s1_index][s2_index + 1]
                        continue
                    
                    dp[s1_index][s2_index][s3_index] = (
                        dp[s1_index + 1][s2_index][s3_index + 1] or
                        dp[s1_index][s2_index + 1][s3_index + 1]
                    )
                    # dp_new[s1_index][s2_index] = (
                    #     dp[s1_index + 1][s2_index] or
                    #     dp[s1_index][s2_index + 1]
                    # )
            
            # Update dp to dp_new!
            # dp = dp_new
        
        # return dp[0][0]
        return dp[0][0][0]

    # Time Complexity:
    #   - O(len(s1) * len(s2) * len(s3)) subproblems
    #   - O(1) time / suproblem
    #   == O(S1 * S2 * S3), where S1 == len(s1), S2 == len(s2), S3 == len(s3)
    def dp3D(self, s1_index, s2_index, s3_index):
        if (s1_index, s2_index, s3_index) in self.memo:
            return self.memo[(s1_index, s2_index, s3_index)]
        
        if s3_index >= len(self.s3):
            return s1_index >= len(self.s1) and s2_index >= len(self.s2)
        
        s1_letter = None if s1_index >= len(self.s1) else self.s1[s1_index]
        s2_letter = None if s2_index >= len(self.s2) else self.s2[s2_index]
        s3_letter = self.s3[s3_index]
        
        if s3_letter != s1_letter and s3_letter != s2_letter:
            return False
        
        if s3_letter != s2_letter:
            res = self.dp3D(s1_index + 1, s2_index, s3_index + 1)
            self.memo[(s1_index, s2_index, s3_index)] = res
            return res
        
        if s3_letter != s1_letter:
            res = self.dp3D(s1_index, s2_index + 1, s3_index + 1)
            self.memo[(s1_index, s2_index, s3_index)] = res
            return res
        
        res = (
            self.dp3D(s1_index + 1, s2_index, s3_index + 1) 
            or self.dp3D(s1_index, s2_index + 1, s3_index + 1)
        )
        self.memo[(s1_index, s2_index, s3_index)] = res
        return res
