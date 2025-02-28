class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        self.str1, self.str2 = str1, str2
        self.memo = {}

        res = []
        i, j = 0, 0
        while True:
            count, (next_i, next_j) = self.dp(i, j)
            if count == 0:
                break

            # Also handles case where both i and j incremented by one, since letter is same!
            res.append(str1[i] if next_i > i else str2[j])

            # Loop Invariant
            i, j = next_i, next_j
            
        return "".join(res)
    
    def dp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        # Constants
        str1, str2 = self.str1, self.str2
        N, M = len(str1), len(str2)
        COUNT, INDICES = 0, 1
        
        # Base Case: Already got all the letters we needed!
        if i >= N and j >= M:
            return (0, (None, None))

        # Base Case: str1 already covered, so only cover rest of str2!
        if i >= N:
            count = 1 + self.dp(i, j + 1)[COUNT]
            res = (count, (i, j + 1))
            self.memo[(i, j)] = res
            return res
        
        # Base Case: str2 already covered, so only cover rest of str1!
        if j >= M:
            count = 1 + self.dp(i + 1, j)[COUNT]
            res = (count, (i + 1, j))
            self.memo[(i, j)] = res
            return res
        
        # Letters are same, so move both at same time!
        letter_i, letter_j = str1[i], str2[j]
        if letter_i == letter_j:
            count = 1 + self.dp(i + 1, j + 1)[COUNT]
            res = (count, (i + 1, j + 1))
            self.memo[(i, j)] = res
            return res
        
        # Letters are not same, so pick whichever index is better to move via DP!
        case_i = 1 + self.dp(i + 1, j)[COUNT]
        case_j = 1 + self.dp(i, j + 1)[COUNT]
        res = (case_i, (i + 1, j)) if case_i < case_j else (case_j, (i, j + 1))
        self.memo[(i, j)] = res
        return res
