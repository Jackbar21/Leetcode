class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)

        k %= sum(chalk)

        i = 0
        # while chalk[i % n] >= k:
        while chalk[i] <= k:
            # print(i, k)
            k -= chalk[i]
            i += 1
            assert i != n
            if i >= n:
                assert i == n
                i = 0
        
        return i