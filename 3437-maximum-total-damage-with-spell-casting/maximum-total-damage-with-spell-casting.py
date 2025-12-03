class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        d = defaultdict(int)
        for p in power:
            d[p] += 1
        self.sorted_power_freqs = [(key, d[key]) for key in sorted(d.keys())]
        self.memo = {}
        return self.dp(0)
    
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]

        sorted_power_freqs = self.sorted_power_freqs
        N = len(sorted_power_freqs)

        if i >= N:
            return 0
        
        # Case 1: Skip index i
        case1 = self.dp(i + 1)

        # Case 2: Choose index i
        # This means you can keep all of same power, but must then skip any that is of
        # power + 1 or power + 2
        power, freq = sorted_power_freqs[i]
        case2 = power * freq

        # Find leftmost index l such that sorted_power_freqs[l][0] > power + 2
        if sorted_power_freqs[N - 1][0] > power + 2:
            l, r = i + 1, N - 1
            while l <= r:
                mid = (l + r) // 2
                if sorted_power_freqs[mid][0] > power + 2:
                    r = mid - 1
                else:
                    l = mid + 1
            case2 += self.dp(l)

        res = case1 if case1 > case2 else case2
        self.memo[i] = res
        return res
