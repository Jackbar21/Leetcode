class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            # If solution, then return
            # if mid > 0 and nums[mid - 1] > nums[mid]:
            #     return nums[mid]

            if nums[0] <= nums[mid]:
                # Current array is strictly increasing.
                # So, pivot MUST have occurred in right subhalf
                l = mid + 1
            else:
                # Pivot must be between l and mid indices,
                # so ignore right subhalf.
                r = mid - 1
        
        print(l, r)
        print(nums)
        # return -1
        return nums[l % len(nums)]