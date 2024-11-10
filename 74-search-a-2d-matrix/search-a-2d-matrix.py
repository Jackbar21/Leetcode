class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # If target less than smallest value or larger than largest value,
        # then we already know that there is NO solution.
        if target <= matrix[0][0] or target >= matrix[-1][-1]:
            return target == matrix[0][0] or target == matrix[-1][-1]
        

        

        # Want to find RIGHTMOST index i such that matrix[i][0] <= target
        # rightmost_index = -1
        # l, r = 0, len(first_col)
        # while l < r:
        #     mid = (l + r) // 2
        #     #print(first_col[mid], target)
        #     if first_col[mid] <= target:
        #         rightmost_index = max(rightmost_index, mid)
        #         l = mid + 1
        #     else:
        #         r = mid - 1

        # Want to find LEFTMOST index i such that matrix[i][0] > target,
        # and from there -- row we want is at index i - 1
        first_col = [matrix[i][0] for i in range(len(matrix))]
        print(f"{first_col=}")
        print(f"{[first_col[mid] > target for mid in range(len(first_col))]}")
        leftmost_index = float("inf")
        l, r = 0, len(first_col) - 1
        while l <= r:
            mid = (l + r) // 2
            is_true = first_col[mid] > target
            if first_col[mid] > target:
                leftmost_index = min(leftmost_index, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        # assert leftmost_index == l
        print(leftmost_index - 1, l, "DSA")
        if l == 0:
            return False
        rightmost_index = l - 1
    
        
        # rightmost_index != -1 thanks to initial check!
        #print(rightmost_index)
        # assert 0 <= rightmost_index < len(matrix)
        # if rightmost_index == -1:
        #     return False
        # if leftmost_index == float("inf"):
        #     return False

        # From this point on, we know that if target exists, it must belong
        # inside row at row-index 'rightmost_index', so regular binary search
        # here will suffice.
        row = matrix[rightmost_index]
        print(f"{row=}")
        l, r = 0, len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                assert row[mid] > target
                r = mid - 1
        
        return False