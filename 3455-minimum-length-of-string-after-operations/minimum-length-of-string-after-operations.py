class Solution:
    def minimumLength(self, s: str) -> int:
        d = defaultdict(int)
        for letter in s:
            d[letter] += 1
        print(f"{d=}")
        # return -1

        return len(d) + sum(d[letter] % 2 == 0 for letter in d)