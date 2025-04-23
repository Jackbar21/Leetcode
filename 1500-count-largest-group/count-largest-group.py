class Solution:
    def countLargestGroup(self, n: int) -> int:
        # groups = defaultdict(int)
        groups = [0] * 37
        for num in range(1, n + 1):
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            groups[digit_sum] += 1
        # max_group_size = max(groups.values())
        # return sum(group_size == max_group_size for group_size in groups.values())
        max_group_size = max(groups)
        return len(list(filter(lambda group_size: group_size == max_group_size, groups)))
