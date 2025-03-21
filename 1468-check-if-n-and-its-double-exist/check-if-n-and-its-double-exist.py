class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        count_zeroes = 0
        for num in arr:
            seen.add(num)
            count_zeroes += (num == 0)

        for num in arr:
            double = 2 * num
            if double in seen and not (double == 0 and count_zeroes <= 1):
                return True
        
        return False