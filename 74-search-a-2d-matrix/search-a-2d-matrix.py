class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        
        # Step 1: Binary search to figure out which row target belongs in
        # Want to find "rightmost" (largest index) row such that row[0] <= target

        l, r = 0, M - 1
        index = None

        while l <= r:
            mid = (l + r) // 2
            row = matrix[mid]

            left, right = row[0], row[N - 1]

            if left <= target <= right:
                index = mid
                break
            
            if target < left:
                r = mid - 1
                continue
            
            assert right < target
            l = mid + 1


        if index is None:
            return False
        
        row = matrix[index]
        # Now, if target exists, it's in this row 'row'
        # Let's binary search to see if it's there!
        l, r = 0, N - 1
        while l <= r:
            mid = (l + r) // 2
            num = row[mid]

            if num == target:
                return True
            
            if target < num:
                r = mid - 1
                continue
            
            assert target > num
            l = mid + 1
        
        return False