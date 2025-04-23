class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)
        for num in range(1, n + 1):
            digit_sum = sum(map(int, str(num)))
            groups[digit_sum] += 1
        max_group_size = max(groups.values())
        return sum(group_size == max_group_size for group_size in groups.values())
