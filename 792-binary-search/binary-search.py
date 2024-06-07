class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        
        if target < nums[mid]:
            return self.search(nums[:mid], target)
        
        # target > nums[mid]
        res = self.search(nums[mid+1:], target)
        return (mid+1+res) if res != -1 else -1