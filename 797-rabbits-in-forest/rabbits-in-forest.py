class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = defaultdict(int)
        for answer in answers:
            d[answer] += 1
        # print(f"{d=}")

        # For '0' -> we take the count
        # For '1' -> we take 2 * math.ceil(count / 2)

        res = 0
        for answer, count in d.items():
            res += (answer + 1) * math.ceil(count / (answer + 1))
        return res
