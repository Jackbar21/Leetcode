class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[0] <= nums[mid]:
                # Current array is increasing, so
                # pivot MUST have occurred in right subhalf
                l = mid + 1
            else:
                # Pivot must be between l and mid indices,
                # so ignore right subhalf.
                r = mid - 1
        
        return nums[l % len(nums)]