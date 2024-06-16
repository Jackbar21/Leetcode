class Solution:
    def binarySearch(self, arr, target):
        if len(arr) <= 0:
            return False
        
        if len(arr) == 1:
            return arr[0] == target
        
        mid = len(arr) // 2
        if arr[mid] == target:
            return True
        
        if target < arr[mid]:
            return self.binarySearch(arr[:mid], target)
        
        return self.binarySearch(arr[mid+1:], target)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) <= 0:
            return False
        
        if len(matrix) == 1:
            return self.binarySearch(matrix[0], target)
        
        mid = len(matrix) // 2
        low, high = matrix[mid][0], matrix[mid][-1]

        if low <= target <= high:
            return self.binarySearch(matrix[mid], target)
        
        if target < low:
            return self.searchMatrix(matrix[:mid], target)
        
        if target > high:
            return self.searchMatrix(matrix[mid+1:], target)
        
        raise Exception("Not reachable")