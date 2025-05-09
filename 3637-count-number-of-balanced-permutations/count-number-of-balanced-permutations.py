class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        # self.editorial(num) is copy pasted function from the Editorial solutions
        # Below this is a correct brute-force approach via backtracking that obviously TLEs.
        # I'm taking the L on the problem, I hope you may understand :)
        return self.editorial(num)

        N = len(num)
        MOD = pow(10, 9) + 7

        total_sum = sum(int(digit) for digit in num)
        if total_sum % 2 == 1:
            return 0

        d = defaultdict(int)
        for digit in num:
            d[int(digit)] += 1
        
        arr = []
        self.cur_sum = 0
        self.res = 0
        def backtrack(i):
            if self.cur_sum > total_sum:
                return

            if i >= N:
                if self.cur_sum == 0:
                    self.res += 1
                return
            
            for digit, freq in d.items():
                if freq > 0:
                    # Setup!
                    d[digit] -= 1
                    if i % 2 == 0:
                        self.cur_sum += digit
                    else:
                        self.cur_sum -= digit

                    # Backtrack!
                    backtrack(i + 1)

                    # Undo!
                    d[digit] += 1
                    if i % 2 == 0:
                        self.cur_sum -= digit
                    else:
                        self.cur_sum += digit
        
        backtrack(0)
        return self.res % MOD
    
    def editorial(self, num: str) -> int:
        MOD = 10**9 + 7
        num = list(map(int, num))
        tot = sum(num)
        if tot % 2 != 0:
            return 0
        target = tot // 2
        cnt = Counter(num)
        n = len(num)
        maxOdd = (n + 1) // 2
        psum = [0] * 11
        for i in range(9, -1, -1):
            psum[i] = psum[i + 1] + cnt[i]

        @cache
        def dfs(pos, curr, oddCnt):
            # If the remaining positions cannot complete a legal placement, or the sum of the elements in the current odd positions is greater than the target value
            if oddCnt < 0 or psum[pos] < oddCnt or curr > target:
                return 0
            if pos > 9:
                return int(curr == target and oddCnt == 0)
            evenCnt = (
                psum[pos] - oddCnt
            )  # Even-numbered positions remaining to be filled
            res = 0
            for i in range(
                max(0, cnt[pos] - evenCnt), min(cnt[pos], oddCnt) + 1
            ):
                # Place i of the current number at odd positions, and cnt[pos] - i at even positions
                ways = comb(oddCnt, i) * comb(evenCnt, cnt[pos] - i) % MOD
                res += ways * dfs(pos + 1, curr + i * pos, oddCnt - i)
            return res % MOD

        return dfs(0, 0, maxOdd)
