class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = pow(10, 9) + 7
        # self.MOD = MOD
        # self.memo = {}

        # Step 1: Count how many possible strings Alice 
        #         could have typed (i.e. k == 1). 
        freq = []
        running_count = 1
        prev_letter = word[0]
        for i in range(1, len(word)):
            letter = word[i]
            if letter == prev_letter:
                running_count += 1
                continue
            freq.append(running_count)
            prev_letter = letter
            running_count = 1
        freq.append(running_count)
        # self.freq = freq
        total_possibilities = functools.reduce(lambda x, y: (x * y) % MOD, freq)

        # Step 2: Since want strings of length at least k, let's count strings
        # of length 1, length 2, ..., length k - 1 that are possible, and
        # subtract them from total possibilities count!

        # TOP-DOWN DP:
        # res = total_possibilities
        # for length in range(1, k):
        #     count = self.dp(0, length)
        #     res -= count
        # return res % MOD

        # BOTTOM-UP DP:
        N = len(freq)
        if N >= k:
            return total_possibilities

        dp = [[0] * k for _ in range(N + 1)]

        # Base Case 1: (Remaining Count == 0)
        # for i in range(N):
        #     dp[i][0] = 0

        # Base Case 2:
        # freq_count = freq[N - 1]
        # for remaining_count in range(1, k):
        #     dp[N - 1][remaining_count] = 1 if freq_count >= remaining_count else 0
        dp[N][0] = 1
        
        for i in range(N - 1, -1, -1):
            freq_count = freq[i]
            prefix_sums = []
            cur_sum = 0
            for remaining_count in range(k):
                cur_sum += dp[i + 1][remaining_count]
                cur_sum %= MOD
                prefix_sums.append(cur_sum)

            for remaining_count in range(1, k):
                min_count = freq_count if freq_count < remaining_count else remaining_count
                # for count in range(1, min_count + 1):
                #     case_count += dp[i + 1][remaining_count - count]
                #     case_count %= MOD
                # Range is [remaining_count - min_count, remaining_count - 1]
                # So just use above prefix sums!
                l, r = remaining_count - min_count, remaining_count - 1
                case_count = prefix_sums[r] - (prefix_sums[l - 1] if l - 1 >= 0 else 0)
                dp[i][remaining_count] = case_count % MOD

        # print(f"{dp=}")
        # for i, row in enumerate(dp):
        #     print(f"{i=}: {row}")
        # print()
        # for i in range(N):
        #     print(f"{i=}: {[self.dp(i, remaining_count) for remaining_count in range(k)]}")
        res = total_possibilities
        for length in range(1, k):
            # count = self.dp(0, length)
            count = dp[0][length]
            res -= count
        return res % MOD
    
    def dp(self, i: int, remaining_count: int):
        # Count number of strings from index i onwards that can be created
        # with 'remaining_count' many characters. Essentially, if next character
        # is same as current character, we can choose to include or skip current
        # character. If next character is DIFFERENT, we must include current character...
        # if haven't picked one of current character already (at_least_one bool), or can
        # skip if have

        # Base Case 1:
        if remaining_count == 0:
            return 0 # Still need to use groups, but no characters remaining!

        # Base Case 2:
        freq = self.freq
        N = len(freq)
        freq_count = freq[i]
        if i == N - 1:
            # We're at last character group. We must use up all remaining_count characters
            # from remaining group, so there's 1 way if have enough characters (otherwise
            # 0 since not possible solution!)
            return 1 if freq_count >= remaining_count else 0

        if (i, remaining_count) in self.memo:
            return self.memo[(i, remaining_count)]

        # Here, we must pick how many characters we wish to use
        MOD = self.MOD
        res = 0
        min_count = freq_count if freq_count < remaining_count else remaining_count
        for count in range(1, min_count + 1):
            res += self.dp(i + 1, remaining_count - count)
            res %= MOD
        self.memo[(i, remaining_count)] = res
        return res
