class Solution:
    def __init__(self):
        self.s = None
        self.memo = {}
        self.letters = None
    def strangePrinter(self, s: str) -> int:
        new_s = [s[0]]
        for i in range(1, len(s)):
            if s[i] != new_s[-1]:
                new_s.append(s[i])
        self.s = ''.join(new_s)
        # print(self.s)
        s = self.s
        self.letters = set(s)
        
        return self.strangePrinterDp(0, len(self.s) - 1)
        # # res = self.strangePrinter(0, len(s)-1)
        res = float("inf")
        for pivot in range(len(self.s)):
            # print(s[:pivot]
            # , s[pivot:])

            # print(
            #     self.strangePrinterDp(0, pivot), 
            #     self.strangePrinterDp(pivot, len(s))
            # )

            res = min(res,
                self.strangePrinterDp(0, pivot) + self.strangePrinterDp(pivot, len(self.s) - 1)
            )
        
        return res - 1

    def strangePrinterDp(self, i, j):
        # considers self.s[i: j+1], i.e. where index j is included but not j+1.
        if i > j:
            return 0
        
        print(i,j,len(self.s))
        assert 0 <= i <= j < len(self.s)
        
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        # Base case, absorb cost of printing first character, and then rest recursively.
        res = 1 + self.strangePrinterDp(i + 1, j)

        # Now, we recognize that if a string (of length n) starts and ends with the same
        # letter, then we can print n characters of that letter, and recursively solve
        # the same problem between the second and second to last letters. This makes it so
        # that we don't have to invest 2 printer turns to print the first and n'th character,
        # but rather just 1 turn. This is the means by which how the minimum number of turns
        # may be made smaller than the actual amount of letters in the problem. We can apply
        # this idea from the letter at index i, with any other index after i that contains
        # the exact same letter.

        for pivot in range(i + 1, j + 1):
            if self.s[i] == self.s[pivot]:
                # Apply idea here, since indices i and pivot contain
                # same letter. The idea is to keep moving rightwards from
                # i as well, to eventually reach termination of the problem.

                # This will consider 1 + dp[i+1, pivot-1] as first case, 
                # so will correctly compute best result
                idea = self.strangePrinterDp(i, pivot - 1) 
                rest = self.strangePrinterDp(pivot + 1, j)
                res = min(res, idea + rest)

        self.memo[(i, j)] = res
        return res

        for pivot in range(i + 1, j - 1):
            # print(s[:pivot]
            # , s[pivot:])

            res = min(res,
                self.strangePrinterDp(i, pivot) + self.strangePrinterDp(pivot, j)
            )


            # print(
            #     self.strangePrinterDp(0, pivot), 
            #     self.strangePrinterDp(pivot, len(s))
            # )



        
        # return (self.s[i:j])
        self.memo[(i, j)] = res
        return res