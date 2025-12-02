class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        self.energy, self.k = energy, k
        return max(self.dp(i) for i in range(len(energy)))
    
    @cache
    def dp(self, i):
        energy, k = self.energy, self.k
        N = len(energy)

        if i >= N:
            return 0
        
        return self.energy[i] + self.dp(i + k)