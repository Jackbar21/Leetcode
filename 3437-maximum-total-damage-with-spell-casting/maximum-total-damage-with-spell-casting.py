class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        d = defaultdict(int)
        for p in power:
            d[p] += 1
        self.sorted_power_freqs = [(key, d[key]) for key in sorted(d.keys())]
        return self.dp(0)
    
    @cache
    def dp(self, i):
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
        index = i
        while index < N and sorted_power_freqs[index][0] <= power + 2:
            index += 1
        case2 = power * freq + self.dp(index)

        return max(case1, case2)
