class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for num in arr:
            d[num] = d.get(num, 0) + 1
        
        return max((key for key in d if d[key] == key), default = -1)