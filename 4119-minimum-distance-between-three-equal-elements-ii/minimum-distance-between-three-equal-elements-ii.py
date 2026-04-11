class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res = float("inf")

        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)
        
        for indices in d.values():
            if len(indices) <= 2:
                continue
            
            index = 2
            while index < len(indices):
                i, j, k = indices[index - 2], indices[index - 1], indices[index]
                distance = abs(i - j) + abs(j - k) + abs(k - i)
                if distance < res:
                    res = distance
                index += 1
    
        return res if res != float("inf") else -1