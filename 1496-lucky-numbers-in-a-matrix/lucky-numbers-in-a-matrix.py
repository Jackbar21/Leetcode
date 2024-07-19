class Solution:
    # returns index of smallest element in arr, -1 if arr is empty
    def getMinIndex(self, arr):
        min_num = float("inf")
        index = -1
        for i in range(len(arr)):
            if arr[i] < min_num:
                min_num = arr[i]
                index = i
        return index
    def getMaxIndex(self, arr):
        max_num = float("-inf")
        index = -1
        for i in range(len(arr)):
            if arr[i] > max_num:
                max_num = arr[i]
                index = i
        return index
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # at most min(m,n)
        lucky_contenders = []
        for row_num in range(len(matrix)):
            row = matrix[row_num]
            col_num = self.getMinIndex(row)
            lucky_contenders.append((row_num, col_num))
        
        print(lucky_contenders)
        #  3  7  8
        #  9 11 13
        # 15 16 17
        
        res = set()
        for col_num in range(len(matrix[0])):
            col = [row[col_num] for row in matrix]
            print(col)
            row_num = self.getMaxIndex(col)
            print((row_num, col_num))
            if (row_num, col_num) in lucky_contenders:
                res.add(matrix[row_num][col_num])
        
        return list(res)
            
