class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # 0 ^ 1 == 1
        # 1 ^ 1 == 0

        # For each row, store:
        # (1) its indices with value 0
        # (2) its indices with value 1

        # 0 0 0 |
        # 0 0 1 |
        # 1 1 0 |

        # Always choose key where first digit/char is a '1'
        d = defaultdict(int)

        for row in matrix:
            binary = (
                tuple((digit) for digit in row)
                if row[0] == 1
                else tuple((digit ^ 1) for digit in row)
            )
            d[binary] += 1
        
        return max(d.values())




