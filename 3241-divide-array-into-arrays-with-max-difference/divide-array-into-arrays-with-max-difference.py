class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(1, len(nums), 3):
            small, mid, big = nums[i - 1], nums[i], nums[i + 1]
            arr = [small, mid, big]
            if big - small > k:
                return []
            res.append(arr)
        return res