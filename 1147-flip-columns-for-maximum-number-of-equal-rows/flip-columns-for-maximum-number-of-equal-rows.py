class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # Always choose key where first digit/char is a '1'
        d = {}
        res = 1
        for row in matrix:
            binary = (
                tuple(digit for digit in row)
                if row[0] == 1
                else tuple(digit ^ 1 for digit in row)
            )
            new_val = d.get(binary, 0) + 1
            d[binary] = new_val
            res = max(res, new_val)
        
        return res
