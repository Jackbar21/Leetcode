class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Flatten matrix to an m * n row, and apply regular binary search!
        arr = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i]))]
        # print(arr)
        # return False
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] < target:
                l = mid + 1
            elif arr[mid] > target:
                r = mid - 1
            else:
                return True
        return False

        # Want to find LEFTMOST index i such that matrix[i][0] > target,
        # and from there -- row we want is at index i - 1
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1

        # If l == 0, this means that matrix[0][0] > target, i.e. the smallest value
        # in the entire matrix is larger than target. Therefore, it must be that EVERY
        # value in matrix is larger than target, hence NO value in matrix is EQUAL to target.
        if l == 0:
            return False

        # Otherwise, if target exists, it must exist inside row at index (l - 1)!
        # Hence, regular binary search here will suffice.
        row = matrix[l - 1]
        l, r = 0, len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] < target:
                l = mid + 1
            elif row[mid] > target:
                r = mid - 1
            else:
                # assert row[mid] == target:
                return True
        
        return False
