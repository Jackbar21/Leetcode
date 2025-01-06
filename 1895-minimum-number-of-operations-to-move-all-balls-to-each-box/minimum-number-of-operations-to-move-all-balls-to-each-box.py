class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)

        prefix_sums = [0]
        count = 0
        for digit in boxes:
            count += digit == "1"
            prefix_sums.append(prefix_sums[-1] + count)
        # prefix_sums.pop()
        
        suffix_sums = [0]
        count = 0
        for digit in reversed(boxes):
            count += digit == "1"
            suffix_sums.append(suffix_sums[-1] + count)
        # suffix_sums.pop()

        return [prefix_sums[i] + suffix_sums[N - 1 - i] for i in range(N)]
