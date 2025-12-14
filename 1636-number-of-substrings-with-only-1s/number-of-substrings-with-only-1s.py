class Solution:
    def numSub(self, s: str) -> int:
        MOD = pow(10, 9) + 7
        res = group_size = 0
        for char in s:
            if char == "1":
                group_size += 1
            else:
                res += (group_size * (group_size + 1)) // 2
                group_size = 0

        res += (group_size * (group_size + 1)) // 2
        return res % MOD
