class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if all(digit == 9 for digit in digits):
            return [1] + [0] * len(digits)
        
        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i]
            if digit < 9:
                digits[i] += 1
                break
            
            # Carry the '1' over to the next (higher-significant) digit
            digits[i] = 0
        
        return digits
