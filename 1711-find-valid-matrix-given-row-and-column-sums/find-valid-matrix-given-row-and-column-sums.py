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
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = [[0] * len(colSum) for i in range(len(rowSum))]

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
            
            # Loop Invariant
            row_sum -= sum_to_add
            col_sum -= sum_to_add
        
        return matrix