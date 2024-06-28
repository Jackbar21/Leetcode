class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = math.floor(len(nums)/2)
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1
            if d[num] > maj:
                return num
        raise Exception("Not Reachable")
        