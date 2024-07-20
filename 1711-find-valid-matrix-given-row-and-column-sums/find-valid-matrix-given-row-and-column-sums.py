class Solution:
    def argMinNonZero(self, arr):
        min_el = float("inf")
        index = -1
        for i in range(len(arr)):
            if arr[i] != 0 and arr[i] < min_el:
                assert arr[i] > 0
                index = i
                min_el = arr[i]
        return index
    def argMax(self, arr):
        max_el = float("-inf")
        index = -1
        for i in range(len(arr)):
            if arr[i] > max_el:
                index = i
                max_el = arr[i]
        return index
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # TODO: verify if should be len colSum then rowSum, or vice versa
        matrix = [[0] * len(colSum) for i in range(len(rowSum))]

        # cur_sum = 0
        row_sum = sum(rowSum)
        col_sum = sum(colSum)

        while row_sum + col_sum > 0:
            row_index = self.argMinNonZero(rowSum)
            col_index = self.argMinNonZero(colSum)
            row_val, col_val = rowSum[row_index], colSum[col_index]

            sum_to_add = min(row_val, col_val)
            rowSum[row_index] -= sum_to_add
            colSum[col_index] -= sum_to_add
            matrix[row_index][col_index] += sum_to_add
            row_sum -= sum_to_add
            col_sum -= sum_to_add
        
        return matrix
        

# matrix =
# | 3  0 |
# | 1  7 |

# cur_sum = 3 + 1 + 7 = 11
# total_sum = 3 + 8 + 4 + 7 = 11 + 
# rowSum = [0, 0]
# colSum = [0, 0]