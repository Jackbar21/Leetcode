class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Helper
        def plusOneRec(digits, index):
            if digits[index] < 9:
                digits[index] += 1
                return digits
            
            digits[index] = 0
            if index == 0:
                return [1] + digits
            return plusOneRec(digits, index - 1)
        
        return plusOneRec(digits, len(digits) - 1)