class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        max_freq = 0
        for num in nums:
            freq = d.get(num, 0) + 1
            d[num] = freq
            if max_freq < freq:
                max_freq = freq
        
        res = 0
        for freq in d.values():
            res += freq == max_freq
        return res * max_freq