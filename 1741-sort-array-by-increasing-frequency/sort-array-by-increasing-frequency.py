class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        max_freq = 0
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
            max_freq = max(max_freq, d[num])
        print(d)
        frequencies = {
            i: [] for i in range(1,max_freq+1)
        }

        
        for num in d:
            frequencies[d[num]].append(num)
        print(frequencies)
        for key in frequencies:
            frequencies[key] = sorted(frequencies[key], reverse=True)
        print(frequencies)
        res = []
        for frequency in range(1,max_freq+1):
            for num in frequencies[frequency]:
                # for _ in range(frequency):
                #     res.append(num)
                res += [num]*frequency
        
        return res

