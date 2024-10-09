class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # BAD: O(nlogn)
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        return sorted(set(nums), key=lambda num: d[num])[-k:]