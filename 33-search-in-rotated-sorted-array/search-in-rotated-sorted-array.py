class Solution:
    def binarySearch(self, l, r, nums, target):
        while l <= r:
            mid = (l + r) // 2
            num = nums[mid]

            if num < target:
                l = mid + 1
            elif num > target:
                r = mid - 1
            else:
                # assert num == target
                return mid
    
        return -1

    def search(self, nums: List[int], target: int) -> int:
        min_index = self.findMin(nums)

        res = self.binarySearch(0, min_index - 1, nums, target)
        if res != -1:
            return res
        
        return self.binarySearch(min_index, len(nums) - 1, nums, target)

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[0] <= nums[mid]:
                return self.binarySearch(0, mid, nums, target)
            

        
        return l
    

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
        
        # return nums[l % len(nums)]
        return l % len(nums)