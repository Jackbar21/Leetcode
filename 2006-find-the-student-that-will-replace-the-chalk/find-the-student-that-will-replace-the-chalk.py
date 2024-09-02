class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)

        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k -= chalk[i]

        raise Exception("Unreachable code")