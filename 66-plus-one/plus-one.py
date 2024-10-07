class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if all(digit == 9 for digit in digits):
            return [1] + [0] * len(digits)
        
        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i]
            if digit == 9:
                digits[i] = 0
                # if i == 0:
                #     return [1] + digits
                continue
            
            digits[i] += 1
            break
        
        return digits