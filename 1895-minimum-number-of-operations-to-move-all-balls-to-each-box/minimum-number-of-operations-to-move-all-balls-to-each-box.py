class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)

        prefix_sums, suffix_sums = [0], [0]
        prefix_count, suffix_count = 0, 0
        for digit in boxes:
            prefix_count += digit == "1"
            prefix_sums.append(prefix_sums[-1] + prefix_count)
        for digit in reversed(boxes):
            suffix_count += digit == "1"
            suffix_sums.append(suffix_sums[-1] + suffix_count)

        return [prefix_sums[i] + suffix_sums[N - 1 - i] for i in range(N)]
