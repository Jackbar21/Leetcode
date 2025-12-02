class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        N = len(energy)
        for i in range(N - 1 - k, -1, -1):
            energy[i] += energy[i + k]
        return max(energy)
