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
            d[binary] = d.get(binary, 0) + 1
            res = max(res, d[binary])
            # d[binary] = new_val
        
        return res
