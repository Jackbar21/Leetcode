class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0

        for detail in details:
            assert len(detail) == 15
            first, second = int(detail[-4]), int(detail[-3])
            if first > 6 or first == 6 and second > 0:
                count += 1

        return count