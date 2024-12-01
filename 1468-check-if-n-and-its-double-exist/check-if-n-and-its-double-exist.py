class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set(arr)
        count_zeroes = arr.count(0)

        for num in arr:
            double = 2 * num
            if double in seen:
                if double == 0 and count_zeroes <= 1:
                    pass
                else:
                    return True
        
        return False