class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(1, len(nums), 3):
            prev, cur, nxt = nums[i - 1], nums[i], nums[i + 1]
            arr = [prev, cur, nxt]
            if max(arr) - min(arr) > k:
                return []
            res.append(arr)
        return res