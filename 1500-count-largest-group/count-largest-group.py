class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)
        for num in range(1, n + 1):
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            groups[digit_sum] += 1

        res = 0
        largest_size = max(groups.values())
        for group_size in groups.values():
            if group_size == largest_size:
                res += 1
        return res
