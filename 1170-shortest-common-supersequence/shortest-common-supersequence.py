class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        self.str1, self.str2 = str1, str2
        self.memo = {}
        # count, _ = self.dp(0, 0)

        # Populate self.memo
        # self.dp(0, 0)
        # print(f"{self.memo=}")

        # dp = self.memo

        res = []
        i, j = 0, 0
        while True:
            count, (next_i, next_j) = self.dp(i, j)
            print(f"{count=}, {next_i=}, {next_j=}")
            if count == 0:
                break
            
            # Also handles case where both i and j incremented by one, since letter is same!
            if next_i - i > 0:
                res.append(str1[i])
            else:
                res.append(str2[j])
            
            i, j = next_i, next_j
            

        print(f"{res=}")
        print(f"{count=}")
        return "".join(res)
            
        

        return res[0]
        # max_length = len(str1) + len(str2)

        # best_i, best_j = None, None
        # res = float("inf")
        # for i in range(max_length):
        #     for j in range(i + 1, max_length):
        #         length = 
                
    def dp(self, i, j):
        # print(f"{self.memo=}")
        str1, str2 = self.str1, self.str2
        N, M = len(str1), len(str2)
        COUNT, INDICES = 0, 1

        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        if i >= N and j >= M:
            return (0, (i, j))

        if i >= N:
            res = 1 + self.dp(i, j + 1)[COUNT]
            self.memo[(i, j)] = (res, (i, j + 1))
            return self.memo[(i, j)]
        
        if j >= M:
            res = 1 + self.dp(i + 1, j)[COUNT]
            self.memo[(i, j)] = (res, (i + 1, j))
            return self.memo[(i, j)]
        
        letter_i, letter_j = str1[i], str2[j]
        if letter_i == letter_j:
            res = 1 + self.dp(i + 1, j + 1)[COUNT]
            self.memo[(i, j)] = (res, (i + 1, j + 1))
            return self.memo[(i, j)]
        
        case_i = 1 + self.dp(i, j + 1)[COUNT]
        case_j = 1 + self.dp(i + 1, j)[COUNT]
        self.memo[(i, j)] = (case_i, (i, j + 1)) if case_i < case_j else (case_j, (i + 1, j))
        return self.memo[(i, j)]


    # @cache
    # def dp(self, i, j):
    #     # Returns tuple where first entry is smallest length, second entry is True if i was incremented,
    #     # else False if j was incremented
    #     str1, str2 = self.str1, self.str2
    #     N, M = len(str1), len(str2)
    #     if i >= N:
    #         # Need to add remaining characters from str2!
    #         string = str2[j:]
    #         assert len(string) == M - j
    #         return (M - j, string)
        
    #     if j >= M:
    #         string = str1[i:]
    #         assert len(string) == N - i
    #         return (N - i, string)
        
    #     letter_i, letter_j = str1[i], str2[j]
    #     if letter_i == letter_j:
    #         res = 1 + self.dp(i + 1, j + 1)[0]
    #         self.memo[(i, j)] = (res, letter_i) # both letters same
    #         return self.memo[(i, j)]
        
    #     # res = min(
    #     #     1 + self.dp(i, j + 1),
    #     #     1 + self.dp(i + 1, j)
    #     # )
    #     case_i = 1 + self.dp(i, j + 1)[0]
    #     case_j = 1 + self.dp(i + 1, j)[0]
    #     res = (case_i, letter_i) if case_i < case_j else (case_j, letter_j)
    #     self.memo[(i, j)] = res
    #     return res


