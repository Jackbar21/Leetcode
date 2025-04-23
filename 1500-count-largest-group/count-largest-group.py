class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)
        max_group_size = 0
        for num in range(1, n + 1):
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            groups[digit_sum] += 1

            # Update max group size
            group_size = groups[digit_sum]
            if max_group_size < group_size:
                max_group_size = group_size

        return sum(map(lambda group_size: group_size == max_group_size, groups.values()))
