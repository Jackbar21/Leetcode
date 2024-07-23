class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        max_freq = 0
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
            max_freq = max(max_freq, d[num])
        
        frequencies = {
            i: [] for i in range(1,max_freq+1)
        }

        
        for num in d:
            for _ in range(d[num]):
                frequencies[d[num]].append(num)
        
        res = []
        for i in range(1,max_freq+1):
            res += sorted(frequencies[i], reverse=True)
        
        return res

