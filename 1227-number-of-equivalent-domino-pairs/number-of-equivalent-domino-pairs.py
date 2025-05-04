class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = defaultdict(int)
        for a, b in dominoes:
            small, big = (a, b) if a < b else (b, a)
            d[(small, big)] += 1

        return sum((n * (n - 1)) // 2 for n in d.values())
