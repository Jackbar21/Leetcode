class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        assert n >= 2

        odd_neg = 0 # 0 means False/even, 1 means True/odd
        zeroes = 0 # True iff at least one zero in matrix
        smallest_magnitude = float("inf") # (i.e. smallest number when absolute value'd)

        res = 0
        for i in range(n):
            for j in range(n):
                num = matrix[i][j]
                smallest_magnitude = min(smallest_magnitude, abs(num))
                if num <= 0:
                    odd_neg ^= 1 # Flip the bit!
                    zeroes |= (num == 0)
                    res -= num
                else:
                    res += num
                    
        
        if not zeroes and odd_neg:
            # res += largest_neg
            # res += largest_neg
            res -= 2 * smallest_magnitude
        
        return res

        

        # So if two negative numbers are in the same row,  I can make them positive
        # Likewise, if two negative numbers are in same col, can make them positive
        # 1 2 3

        # +A +B +C
        # +D +E +F
        # +G +H +I

        # -1 +0 -1
        # -2 +1 +3
        # +3 +2 +2

        # +2 +9 +3
        # +5 +4 -4
        # +1 +7 +1