class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0

        for detail in details:
            first_digit, second_digit = int(detail[-4]), int(detail[-3])
            if first_digit > 6 or first_digit == 6 and second_digit > 0:
                count += 1

        return count