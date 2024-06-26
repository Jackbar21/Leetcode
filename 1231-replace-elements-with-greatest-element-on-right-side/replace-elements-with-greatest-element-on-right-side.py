class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) <= 0:
            return []
        
        if len(arr) == 1:
            return [-1]
        
        biggest = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            tmp = arr[i]
            arr[i] = biggest
            biggest = max(biggest, tmp)
        return arr