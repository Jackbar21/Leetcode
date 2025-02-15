class Solution:
    def canPartition(self, num: int, target: int) -> bool:
        # self.memo = {}
        # self.str_num = str(num)
        # self.res = False
        str_num = str(num)
        res = [[]]

        def backtrack(i):
            if i == len(str_num):
                val = sum(int("".join(group)) for group in res if group != [])
                return val == target
            
            # Get i'th digit
            digit = str_num[i]

            # Case 1: Add it to current last group
            res[-1].append(digit)
            if backtrack(i + 1):
                return True
            res[-1].pop()

            # Case 2: Add it to new group
            res.append([digit])
            if backtrack(i + 1):
                return True
            res.pop()

            # Neither case was successful, hence no possible solution...
            return False
        
        return backtrack(0)


        str_num = str(num)
        for digit in str_num:
            # Case 1: Add it to current last group
            backtrack[-1].append(digit)

            # Case 2: Add it to new group


    def dp(self, i, j):
        # Index i represents the last time we did a cutoff. Index j is our current index,
        # and we can either choose to cutoff here, or keep growing the index.
        # If we're at the very last index, we have no choice but to do a cutoff
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        # if 

        # if self.res:
        #     return #?
        

        


        

    def punishmentNumber(self, n: int) -> int:
        res = 0
        for num in range(1, n + 1):
            square = pow(num, 2)
            if self.canPartition(square, num):
                res += square
        return res