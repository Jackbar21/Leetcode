class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        odd_neg = False # 0 means False/even, 1 means True/odd
        smallest_magnitude = float("inf") # (i.e. smallest number when absolute value'd)

        res = 0
        for row in matrix:
            for num in row:
                magnitude = abs(num)
                if smallest_magnitude > magnitude:
                    smallest_magnitude = magnitude

                if num < 0:
                    odd_neg = not odd_neg
                
                res += magnitude
                    
        if odd_neg:
            res -= 2 * smallest_magnitude
        
        return res
